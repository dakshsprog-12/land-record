from app.ocr.engine import OCREngine
from app.pdf.processor import convert_pdf_to_images
from app.layout.line_grouping import group_into_lines
from app.layout.spatial import enrich_lines
from app.layout.region_detection import detect_regions
from app.layout.table_detection import detect_table_columns
from app.layout.table_rows import build_table_rows
from app.layout.cell_grouping import get_item_text
from app.layout.table_scoring import calculate_table_score
from app.layout.table_candidates import detect_table_candidates
from app.extraction.key_value import detect_inline_key_values

import os


PDF_PATH = "bhumi_rasid.pdf"
OUTPUT_DIR = "temp_layout"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# PDF → image
images = convert_pdf_to_images(
    PDF_PATH,
    OUTPUT_DIR
)

image_path = images[0]

# OCR
ocr_engine = OCREngine(lang="hi")

results = ocr_engine.process(image_path)

# Remove extremely low-confidence OCR noise
results = [
    item
    for item in results
    if item["confidence"] >= 0.5
]

# Group OCR tokens into lines
lines = group_into_lines(
    results,
    y_tolerance=15
)

lines = enrich_lines(lines)
regions = detect_regions(lines)

print("\nRECONSTRUCTED LAYOUT\n")
print("=" * 100)


for index, line in enumerate(lines, start=1):

    print(
        f"\nLINE {index:03d} | "
        f"Y={line['center_y']:.1f}"
    )

    for item in line["items"]:

        print(
            f"    X={item['x']:4.0f} "
            f"W={item['width']:4.0f} "
            f"| {item['text']} "
            f"| confidence={item['confidence']:.3f}"
        )
        
        
print("\n\nDETECTED REGIONS")
print("=" * 100)

for region_index, region in enumerate(regions, start=1):

    print(
        f"\nREGION {region_index:02d}"
    )

    for line in region:

        text = " | ".join(
            item["text"]
            for item in line["items"]
        )

        print(
            f"    Y={line['center_y']:.1f} | {text}"
        )


print("\n\nTABLE-LIKE COLUMN DETECTION")
print("=" * 100)

for region_index, region in enumerate(regions, start=1):

    columns = detect_table_columns(region)

    print(
        f"\nREGION {region_index:02d}"
    )

    for column in columns:

        print(
            f"    X={column['center_x']:.1f} "
            f"| occurrences={column['occurrences']}"
        )


print("\n\nTABLE ROW STRUCTURE")
print("=" * 100)

for region_index, region in enumerate(regions, start=1):

    columns = detect_table_columns(region)

    if not columns:
        continue

    rows = build_table_rows(region, columns)

    print(f"\nREGION {region_index:02d}")

    for row_index, row in enumerate(rows, start=1):

        print(
            f"\n  ROW {row_index:02d} "
            f"| Y={row['y']:.1f}"
        )

        for column_x, items in row["columns"].items():

            text = get_item_text(items)

            print(
                f"      X={column_x} "
                f"| {text}"
            )

print("\n\nTABLE CANDIDATE SCORING")
print("=" * 100)

for region_index, region in enumerate(regions, start=1):

    columns = detect_table_columns(region)

    score = calculate_table_score(
        region,
        columns
    )

    print(
        f"\nREGION {region_index:02d}"
        f" | rows={len(region)}"
        f" | columns={len(columns)}"
        f" | score={score:.3f}"
    )
    
print("\n\nTABLE CANDIDATES")
print("=" * 100)

table_candidates = detect_table_candidates(
    regions,
    min_score=0.5
)

for candidate in table_candidates:

    print(
        f"\nREGION {candidate['region_index']:02d}"
        f" | score={candidate['score']:.3f}"
        f" | rows={candidate['rows']}"
        f" | columns={len(candidate['columns'])}"
    )

    for column in candidate["columns"]:

        print(
            f"    X={column['center_x']:.1f}"
            f" | occurrences={column['occurrences']}"
        )


print("\n\nINLINE KEY-VALUE CANDIDATES")
print("=" * 100)

key_values = detect_inline_key_values(lines)

for candidate in key_values:

    print(
        f"\nLABEL  : {candidate['label']}"
        f"\nVALUE  : {candidate['value']}"
        f"\nCONF   : {candidate['confidence']:.3f}"
        f"\nX/Y    : "
        f"{candidate['center_x']:.1f}, "
        f"{candidate['center_y']:.1f}"
    )                        