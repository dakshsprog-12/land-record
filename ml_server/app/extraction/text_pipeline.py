from app.extraction.key_value import split_label_value
from app.extraction.label_mapping import normalize_label
from app.validation.fields import validate_land_record


def extract_land_record_from_text(text):
    candidates = []

    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        result = split_label_value(line)

        if result is None:
            continue

        canonical_field = normalize_label(
            result["label"]
        )

        if canonical_field is None:
            continue

        candidates.append({
            "field": canonical_field,
            "value": result["value"],
            "source": "text_extraction"
        })

    record = {}

    for candidate in candidates:
        record[candidate["field"]] = {
            "value": candidate["value"],
            "confidence": None,
            "source": candidate["source"],
            "evidence": {
                "text": candidate["value"]
            }
        }

    validation = validate_land_record(record)

    return {
        "fields": record,
        "validation": validation
    }