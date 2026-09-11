def validate_field(field, value, confidence):
    issues = []

    if value is None or not str(value).strip():
        issues.append("Missing value")

    if confidence < 0.7:
        issues.append("Low OCR confidence")

    numeric_fields = {
        "khata_number",
        "khasra_number",
        "plot_number",
        "jamabandi_number",
    }

    if field in numeric_fields and value:
        if not str(value).replace("/", "").replace("-", "").isdigit():
            issues.append("Expected numeric value")

    if issues:
        return {
            "status": "warning",
            "issues": issues
        }

    return {
        "status": "valid",
        "issues": []
    }


def validate_land_record(record):
    validation = {}

    for field, data in record.items():
        validation[field] = validate_field(
            field,
            data["value"],
            data["confidence"]
        )

    return validation