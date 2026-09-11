from app.ocr.engine import OCREngine
from app.layout.line_grouping import group_into_lines
from app.layout.spatial import enrich_lines
from app.extraction.key_value import (
    detect_inline_key_values,
    attach_continuations
)
from app.extraction.land_record import build_land_record


engine = OCREngine(lang="hi")

results = engine.process("bhumi_rasid.jpeg")

lines = group_into_lines(results)
lines = enrich_lines(lines)

result = detect_inline_key_values(lines)
result = attach_continuations(
    result,
    lines
)

record = build_land_record(result)
print(record)