from report_standard import SCORING_FIELDS
from unit_map import get_room_pod, room_distance, CVU_ROOM_CONNECTIONS

# Which nurse should take which patient?
# Defining functions for the nurse-patient load


def nurse_load_score(nurse):
    """
    Lower score = better nurse to receive next patient.

    Acuity and turnover are weighted more heavily because:
    - acuity = safety
    - turnover = admissions / discharges / transfers
    """
    return (nurse.current_acuity * 2) + (nurse.current_turnover * 2) + nurse.current_weighted


def get_turnover_score(patient):
    """
    Return the turnover score (0-4) based on the patient's turnover value.
    Example:
    STABLE -> 0
    POSSIBLE_TRANSFER -> 1
    TRANSFER_TODAY / DISCHARGE_TODAY -> 2
    NEW_ADMISSION / TRANSFER_TO_FLOOR -> 3
    MULTIPLE_TURNOVER -> 4
    """
    for score, values in SCORING_FIELDS["turnover"].items():
        if patient.turnover in values:
            return score
    return 0

def adjusted_acuity_limit(nurse):
    """
    Returns the safe acuity limit based on nurse experience.
    """
    if nurse.is_new_grad:
        return int(nurse.max_acuity_capacity * 0.7)

    if nurse.experience_level == "Beginner":
        return int(nurse.max_acuity_capacity * 0.8)

    return nurse.max_acuity_capacity

def nurse_is_eligible_for_patient(nurse, patient):
    """
    Hard safety / assignment rules:
    - nurse must be able to take patient by capacity
    - new grad nurses should avoid high acuity patients
    - less experienced cardiology nurses should avoid the heaviest assignments
    - nurses who cannot take admissions should not receive heavy turnover patients
    """

    # Base capacity / refusal check
    if not nurse.can_take_patient(patient):
        return False

    # Experience-adjusted acuity limit
    # This prevents new grads / beginners from being maxed out
    safe_acuity_limit = adjusted_acuity_limit(nurse)

    if nurse.current_acuity + patient.acuity_score > safe_acuity_limit:
        return False

    patient_pod = get_room_pod(patient.room)

    # Pod rule: nurse should only take patients in their assigned pod
    if nurse.pod is not None and patient_pod is not None:
        if nurse.pod != patient_pod:
            return False

    turnover_score = get_turnover_score(patient)

    # Nurses who cannot take admissions should avoid heavy turnover patients
    if turnover_score >= 3 and not nurse.can_take_admission:
        return False

    # New grad restriction for higher acuity patients
    if nurse.is_new_grad and patient.acuity_score >= 6:
        return False

    # Low cardiology experience restriction for very high acuity patients
    if nurse.years_in_cardiology < 1 and patient.acuity_score >= 8:
        return False

    return True


def assignment_fit_score(nurse, patient):
    """
    Lower score = better fit.

    Uses:
    - nurse load
    - empty rooms awaiting admission
    - turnover burden
    - cardiology experience
    - new grad penalty
    - optional learning exposure bonus
    """
    
    score = nurse_load_score(nurse)

    safe_acuity_limit = adjusted_acuity_limit(nurse)
    turnover_score = get_turnover_score(patient)

    # Penalize nurses getting close to their safe limit AFTER taking this patient
    if safe_acuity_limit > 0:
        future_acuity = nurse.current_acuity + patient.acuity_score
        acuity_ratio = future_acuity / safe_acuity_limit
        score += acuity_ratio * 12  # slightly stronger since it's predictive
        #Workload Penalties
        # Penalty for patient turnover burden
        score += turnover_score * 2
        # Penalty for empty rooms already assigned to nurse
        score += nurse.empty_rooms_assigned * 2

    #Experience Penalties
    # Penalty if cardiology experience is limited and patient is heavier
    if patient.acuity_score >= 7 and nurse.years_in_cardiology < 2:
        score += 3

    # Penalty if nurse is a new grad and patient is moderately heavy
    if nurse.is_new_grad and patient.acuity_score >= 6:
        score += 4

    # Small bonus for learning needs if it matches a patient procedure
    # This should never override safety
    if hasattr(patient, "procedures") and isinstance(patient.procedures, list):
        for need in nurse.learning_needs:
            if need in patient.procedures:
                score -= 1
                break

    # Geography penalty: prefer patients close to nurse's current assignment
    if nurse.assigned_patients:
        distances = []

        for assigned_patient in nurse.assigned_patients:
            distance = room_distance(
                patient.room,
                assigned_patient.room,
                CVU_ROOM_CONNECTIONS
            )

            if distance is not None:
                distances.append(distance)

        if distances:
            closest_distance = min(distances)
            farthest_distance = max(distances)

            score += closest_distance * 1
            score += farthest_distance * 2

    return score


def assign_patients_to_nurses(patients, nurses):
    """
    Assign patients to nurses using:
    1. Hard safety filters
    2. Best-fit scoring among eligible nurses
    """
    unassigned_patients = []

    for patient in patients:
        patient.turnover_score = get_turnover_score(patient)
    # Highest acuity patients first
    sorted_patients = sorted(
        patients,
        key=lambda p: (
            p.acuity_score,
            getattr(p, "total_weighted_score", 0),
            get_turnover_score(p)
        ),
        reverse=True
        )
    
    for patient in sorted_patients:
        eligible_nurses = [
            nurse for nurse in nurses
            if nurse_is_eligible_for_patient(nurse, patient)
        ]

        if not eligible_nurses:
            unassigned_patients.append(patient)
            continue

        best_nurse = min(
            eligible_nurses,
            key=lambda nurse: assignment_fit_score(nurse, patient)
        )

        if best_nurse is not None:
            patient.turnover_score = get_turnover_score(patient)
            best_nurse.assign_patient(patient)

    return nurses, unassigned_patients


def detect_unsafe_assignments(nurses):
    """
    Check for unsafe or questionable nurse assignments.
    Returns a list of warning messages.
    """
    warnings = []

    for nurse in nurses:

        # Over capacity by acuity
        safe_acuity_limit = adjusted_acuity_limit(nurse)

        # Over safe acuity limit
        if nurse.current_acuity > safe_acuity_limit:
            warnings.append(
                f"{nurse.name} is over safe acuity capacity "
                f"({nurse.current_acuity}/{safe_acuity_limit})."
            )

        # Over capacity by patient count
        if len(nurse.assigned_patients) > nurse.adjusted_patient_capacity():
            warnings.append(
                f"{nurse.name} is over patient capacity "
                f"({len(nurse.assigned_patients)}/{nurse.adjusted_patient_capacity()})."
            )

        # New grad carrying too much acuity
        if nurse.is_new_grad and nurse.current_acuity > safe_acuity_limit:
            warnings.append(
                f"{nurse.name} is a new grad with a very heavy acuity load "
                f"({nurse.current_acuity}/{safe_acuity_limit})."
            )

        # Light duty nurse still carrying too much
        if nurse.is_light_duty and nurse.current_acuity >= nurse.adjusted_acuity_capacity():
            warnings.append(
                f"{nurse.name} is on light duty but has a heavy assignment."
            )

        # Too much turnover for one nurse
        if nurse.current_turnover >= 6:
            warnings.append(
                f"{nurse.name} has a high turnover burden ({nurse.current_turnover})."
            )

        # Too many admissions / empty rooms burden
        if nurse.empty_rooms_assigned >= 2:
            warnings.append(
                f"{nurse.name} already has multiple empty rooms awaiting possible admissions."
            )

    return warnings