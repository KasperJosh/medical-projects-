from hospital_patient_tracker.report_standard import (
    validate_single_value,
    validate_multi_value,
    get_allowed_values
)

def get_nonempty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def get_int_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid number.")


def get_list_input(prompt):
    value = input(prompt).strip()
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def get_valid_standard_single(field_name, prompt):
    while True:
        value = input(prompt).strip()
        valid, result = validate_single_value(field_name, value)

        if valid:
            return result

        print(f"Invalid {field_name}.")
        print("Allowed values:", ", ".join(get_allowed_values(field_name)))


def get_valid_standard_multi(field_name, prompt):
    while True:
        value = input(prompt).strip()
        valid, result = validate_multi_value(field_name, value)

        if valid:
            return result

        print(f"Invalid {field_name}: {result}")
        print("Allowed values:", ", ".join(get_allowed_values(field_name)))