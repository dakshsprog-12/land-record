from app.layout.line_grouping import group_into_lines
from app.layout.spatial import enrich_lines
from app.extraction.key_value import (
    detect_inline_key_values,
    attach_continuations
)
from app.extraction.land_record import build_land_record
from app.validation.fields import validate_land_record


def extract_land_record(ocr_results):
    # 1. Group OCR items into lines
    lines = group_into_lines(ocr_results)

    # 2. Add spatial information
    lines = enrich_lines(lines)

    # 3. Detect key-value fields
    candidates = detect_inline_key_values(lines)

    # 4. Attach multiline continuations
    candidates = attach_continuations(
        candidates,
        lines
    )

    # 5. Build structured land record
    record = build_land_record(candidates)

    # 6. Validate extracted fields
    validation = validate_land_record(record)

    return {
        "fields": record,
        "validation": validation
    }