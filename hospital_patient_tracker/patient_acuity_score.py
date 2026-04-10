"""
patient_acuity_score.py

Handles:
- acuity scoring categories
- workload scoring categories
- assignment modifiers
- total score calculation
- score classification

Used with Patient objects in the hospital project.
"""


# =========================================================
# A. PATIENT ACUITY CATEGORIES
# =========================================================

PATIENT_ACUITY_CATEGORIES = {
    "hemodynamic_status": {
        "stable": 0,
        "soft_bp_occasional_monitoring_concern": 1,
        "single_low_dose_pressor_or_intermittent_bolus": 2,
        "titrated_pressor_or_ongoing_instability": 3,
        "multiple_pressors_active_bleed_iabp_impella_with_instability": 4
    },

    "cardiac_status": {
        "nsr_controlled_rhythm": 0,
        "stable_monitored_rhythm_issue": 1,
        "af_rvr_frequent_ectopy_frequent_nsvt": 2,
        "significant_arrhythmia_risk_temp_pacer_recurrent_unstable_rhythm": 3,
        "recent_vt_vf_unstable_rhythm_requiring_urgent_intervention": 4
    },

    "respiratory_status": {
        "room_air_low_flow_o2": 0,
        "moderate_o2_needs": 1,
        "hfnc_cpap_bipap": 2,
        "intubated_ventilated_but_stable": 3,
        "ventilated_with_severe_instability_ards_frequent_interventions": 4
    },

    "neurological_status": {
        "alert_and_oriented": 0,
        "mild_confusion_forgetful": 1,
        "delirium_significant_confusion_frequent_reorientation": 2,
        "reduced_loc_sedated_neuro_monitoring": 3,
        "very_low_gcs_neuro_instability_unsafe_cognition": 4
    },

    "renal_fluid_status": {
        "stable": 0,
        "mild_overload_diuresis": 1,
        "strict_io_aki_frequent_output_monitoring": 2,
        "significant_renal_instability": 3,
        "crrt_or_severe_fluid_electrolyte_instability": 4
    },

    "infection_sepsis": {
        "none": 0,
        "suspected_infection_antibiotics": 1,
        "confirmed_infection_needing_close_followup": 2,
        "sepsis": 3,
        "septic_shock": 4
    },

    "lab_instability": {
        "routine_daily_labs": 0,
        "mild_abnormal_labs_occasional_replacement": 1,
        "frequent_electrolyte_replacement_or_repeated_labs": 2,
        "abgs_unstable_critical_labs_q6h_or_more_frequent_checks": 3,
        "severe_lab_instability_requiring_constant_correction": 4
    },

    "safety_risk": {
        "none": 0,
        "standard_fall_risk": 1,
        "high_fall_risk_impulsive": 2,
        "pulling_lines_wandering_major_safety_concerns": 3,
        "restraints_sitter_immediate_danger_to_self_or_staff": 4
    }
}


# =========================================================
# B. NURSING WORKLOAD CATEGORIES
# =========================================================

NURSING_WORKLOAD_CATEGORIES = {
    "medication_complexity": {
        "po_meds_only": 0,
        "simple_iv_meds": 1,
        "multiple_iv_meds_insulin_infusion": 2,
        "one_or_more_titratable_drips": 3,
        "multiple_titratable_drips_high_complexity_med_management": 4
    },

    "monitoring_frequency": {
        "routine_q4h": 0,
        "q2_to_q4h_plus_some_extra_checks": 1,
        "q2h_structured_monitoring": 2,
        "q1h_monitoring": 3,
        "continuous_near_constant_reassessment": 4
    },

    "lines_devices": {
        "basic_peripheral_access_only": 0,
        "foley_or_single_simple_device": 1,
        "central_line_arterial_line_multiple_access_points": 2,
        "temporary_pacer_chest_tubes_complex_drains": 3,
        "iabp_impella_crrt_ecmo": 4
    },

    "mobility": {
        "independent": 0,
        "supervision_minimal_assist": 1,
        "ax1": 2,
        "ax2_heavy_transfer_burden": 3,
        "total_care_q2_turns_broda_bariatric_heavy_workload": 4
    },

    "nutrition": {
        "independent_po": 0,
        "modified_diet_feeding_setup_some_assistance": 1,
        "full_feeding_assist_or_aspiration_precautions": 2,
        "ngt_ogt_peg_feeds_with_management_burden": 3,
        "complex_enteral_feeding_issues_intolerance_frequent_intervention": 4
    },

    "elimination": {
        "independent_no_issue": 0,
        "foley_or_diaper": 1,
        "frequent_incontinent_care_diarrhea": 2,
        "high_output_stool_skin_breakdown_risk_bowel_management_burden": 3,
        "severe_elimination_workload_with_repeated_care_needs": 4
    },

    "procedures_tests_today": {
        "none": 0,
        "minor_test_or_appointment": 1,
        "moderate_procedure_burden_or_multiple_off_unit_tests": 2,
        "angio_pacemaker_cardioversion_dialysis": 3,
        "major_peri_procedural_day_cabg_tavi_first_case_intensity": 4
    },

    "wounds_dressings_other_nursing_tasks": {
        "none_minimal": 0,
        "simple_dressing": 1,
        "difficult_dressing_multiple_wound_care_tasks": 2,
        "trach_care_cardiac_surgery_dressings_chest_drain_burden": 3,
        "extensive_complex_wound_device_care": 4
    },

    "pain_comfort_management": {
        "controlled": 0,
        "occasional_prns": 1,
        "frequent_prns_repeated_reassessment": 2,
        "pca_difficult_pain_control": 3,
        "severe_uncontrolled_pain_demanding_ongoing_intervention": 4
    },

    "communication_complexity": {
        "no_barrier": 0,
        "mild_barrier": 1,
        "language_hearing_vision_barrier_affecting_care": 2,
        "requires_family_translation_or_repeated_alternate_communication": 3,
        "severe_communication_barrier_significantly_delaying_care": 4
    },

    "family_social_complexity": {
        "minimal": 0,
        "some_support_education_needed": 1,
        "frequent_updates_or_emotional_support_burden": 2,
        "high_demand_family_conflict_goals_of_care_intensity": 3,
        "extreme_family_social_burden_dominating_nursing_time": 4
    },

    "behaviour_cooperation": {
        "cooperative": 0,
        "mildly_anxious_repetitive_reassurance_needed": 1,
        "demanding_poor_compliance_emotionally_labile": 2,
        "frequent_refusal_verbal_aggression_constant_calling_delays_care": 3,
        "physically_aggressive_restraints_staff_safety_issue": 4
    }
}


# =========================================================
# C. ASSIGNMENT MODIFIERS
# =========================================================

ASSIGNMENT_MODIFIERS = {
    "isolation_status": {
        "none": 0,
        "contact": 1,
        "droplet_cdiff_higher_ppe_burden": 2,
        "airborne_tb_very_high_burden": 3
    },

    "turnover_risk": {
        "no_expected_move": 0,
        "possible_transfer": 1,
        "discharge_or_transfer_today": 2,
        "new_admission_today": 3,
        "admission_plus_procedural_plus_likely_multiple_transitions": 4
    }
}


SPECIAL_FLAGS = {
    "blood_transfusion": 1,
    "frequent_caller": 1,
    "one_to_one_observation": 2,
    "bariatric_heavy_care": 1,
    "end_of_life_comfort": 2,
    "post_op_fresh_arrival": 2
}


# =========================================================
# ALL CATEGORIES COMBINED
# =========================================================

ALL_SCORING_CATEGORIES = {
    **PATIENT_ACUITY_CATEGORIES,
    **NURSING_WORKLOAD_CATEGORIES,
    **ASSIGNMENT_MODIFIERS
}


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def calculate_patient_acuity_score(selected_options, selected_flags=None):
    """
    Calculates the total acuity score and returns a detailed breakdown.

    Parameters:
        selected_options (dict):
            Example:
            {
                "hemodynamic_status": "single_low_dose_pressor_or_intermittent_bolus",
                "respiratory_status": "hfnc_cpap_bipap",
                "mobility": "ax2_heavy_transfer_burden"
            }

        selected_flags (list):
            Example:
            ["blood_transfusion", "post_op_fresh_arrival"]

    Returns:
        total_score (int)
        breakdown (dict)
    """

    if selected_flags is None:
        selected_flags = []

    total_score = 0
    breakdown = {}

    for main_category, selected_subcategory in selected_options.items():
        if main_category not in ALL_SCORING_CATEGORIES:
            print(f"Warning: '{main_category}' is not a valid category.")
            continue

        category_options = ALL_SCORING_CATEGORIES[main_category]

        if selected_subcategory not in category_options:
            print(f"Warning: '{selected_subcategory}' is not a valid option under '{main_category}'.")
            continue

        score = category_options[selected_subcategory]
        total_score += score

        breakdown[main_category] = {
            "selected_option": selected_subcategory,
            "score": score
        }

    flag_total = 0
    flag_breakdown = {}

    for flag in selected_flags:
        if flag not in SPECIAL_FLAGS:
            print(f"Warning: '{flag}' is not a valid special flag.")
            continue

        score = SPECIAL_FLAGS[flag]
        flag_total += score
        flag_breakdown[flag] = score

    total_score += flag_total

    if flag_breakdown:
        breakdown["special_flags"] = flag_breakdown

    return total_score, breakdown


def get_acuity_level(score):
    """
    Returns a human-readable acuity level based on total score.
    """

    if score <= 10:
        return "Low"
    elif score <= 20:
        return "Moderate"
    elif score <= 30:
        return "High"
    else:
        return "Critical"


def display_available_categories():
    """
    Prints all available categories and options.
    Useful for debugging or building a menu later.
    """

    print("\n===== PATIENT ACUITY / WORKLOAD CATEGORIES =====")
    for category, options in ALL_SCORING_CATEGORIES.items():
        print(f"\n{category}:")
        for option, score in options.items():
            print(f"  - {option} = {score}")

    print("\n===== SPECIAL FLAGS =====")
    for flag, score in SPECIAL_FLAGS.items():
        print(f"  - {flag} = +{score}")


def score_patient(patient, selected_options, selected_flags=None):
    """
    Applies the calculated score directly to a Patient object.

    Requires patient to have:
        patient.acuity_score
        patient.acuity_level
        patient.acuity_breakdown
    """

    score, breakdown = calculate_patient_acuity_score(selected_options, selected_flags)

    patient.acuity_score = score
    patient.acuity_level = get_acuity_level(score)
    patient.acuity_breakdown = breakdown


# =========================================================
# TEST BLOCK
# =========================================================

if __name__ == "__main__":
    example_selected_options = {
        "hemodynamic_status": "titrated_pressor_or_ongoing_instability",
        "cardiac_status": "significant_arrhythmia_risk_temp_pacer_recurrent_unstable_rhythm",
        "respiratory_status": "intubated_ventilated_but_stable",
        "neurological_status": "reduced_loc_sedated_neuro_monitoring",
        "renal_fluid_status": "strict_io_aki_frequent_output_monitoring",
        "infection_sepsis": "suspected_infection_antibiotics",
        "lab_instability": "frequent_electrolyte_replacement_or_repeated_labs",
        "safety_risk": "high_fall_risk_impulsive",
        "medication_complexity": "one_or_more_titratable_drips",
        "monitoring_frequency": "q1h_monitoring",
        "lines_devices": "temporary_pacer_chest_tubes_complex_drains",
        "mobility": "ax2_heavy_transfer_burden",
        "nutrition": "ngt_ogt_peg_feeds_with_management_burden",
        "elimination": "frequent_incontinent_care_diarrhea",
        "procedures_tests_today": "angio_pacemaker_cardioversion_dialysis",
        "wounds_dressings_other_nursing_tasks": "simple_dressing",
        "pain_comfort_management": "frequent_prns_repeated_reassessment",
        "communication_complexity": "mild_barrier",
        "family_social_complexity": "frequent_updates_or_emotional_support_burden",
        "behaviour_cooperation": "mildly_anxious_repetitive_reassurance_needed",
        "isolation_status": "contact",
        "turnover_risk": "possible_transfer"
    }

    example_selected_flags = [
        "blood_transfusion",
        "post_op_fresh_arrival"
    ]

    total_score, breakdown = calculate_patient_acuity_score(
        example_selected_options,
        example_selected_flags
    )

    print("\n===== ACUITY SCORE RESULT =====")
    print("Total Score:", total_score)
    print("Acuity Level:", get_acuity_level(total_score))
    print("Breakdown:", breakdown)