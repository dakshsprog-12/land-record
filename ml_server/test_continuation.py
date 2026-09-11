from app.ocr.engine import OCREngine
from app.layout.line_grouping import group_into_lines
from app.layout.spatial import enrich_lines
from app.extraction.key_value import detect_inline_key_values
from app.extraction.continuation import find_continuation_items


engine = OCREngine(lang="hi")

results = engine.process("bhumi_rasid.jpeg")

lines = group_into_lines(results)
lines = enrich_lines(lines)

fields = detect_inline_key_values(lines)


for field in fields:

    if field["field"] != "address":
        continue

    source_item = None

    for line in lines:
        for item in line["items"]:
            if item["bbox"] == field["bbox"]:
                source_item = item
                break

    if source_item is None:
        continue

    continuations = find_continuation_items(
        source_item,
        lines
    )

    print("FIELD:", field["field"])
    print("VALUE:", field["value"])

    print("CONTINUATIONS:")

    for item in continuations:
        print(item["text"])