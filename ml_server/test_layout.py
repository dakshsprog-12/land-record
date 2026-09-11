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
from app.extraction.spatial_key_value import detect_spatial_key_values
from app.layout.table_regions import detect_table_subregions
from app.layout.table_regions import (
    detect_table_subregions,
    line_matches_columns
)
from app.layout.table_regions import (
    detect_table_subregions,
    line_matches_columns,
    get_line_width
)

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
table_region_indexes = {
    candidate["region_index"]
    for candidate in table_candidates
}

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


print("\n\nSPATIAL KEY-VALUE CANDIDATES")
print("=" * 100)

spatial_key_values = detect_spatial_key_values(
    regions,
    table_region_indexes=table_region_indexes
)

for candidate in spatial_key_values:
    print(
        f"\nLABEL  : {candidate['label']}"
        f"\nVALUE  : {candidate['value']}"
        f"\nLABEL CONF : {candidate['label_confidence']:.3f}"
        f"\nVALUE CONF : {candidate['value_confidence']:.3f}"
        f"\nGAP    : {candidate['horizontal_gap']:.1f}"
    )


print("\nTABLE REGION INDEXES")
print("=" * 100)
print(table_region_indexes)

print("\n\nSPATIAL KEY-VALUE CANDIDATES")
print("=" * 100)

for candidate in spatial_key_values:
    print(
        f"\nREGION : {candidate['region_index']}"
        f"\nLABEL  : {candidate['label']}"
        f"\nVALUE  : {candidate['value']}"
        f"\nLABEL CONF : {candidate['label_confidence']:.3f}"
        f"\nVALUE CONF : {candidate['value_confidence']:.3f}"
        f"\nGAP    : {candidate['horizontal_gap']:.1f}"
    )

print("\nDETECTED TABLE COLUMNS")

for candidate in table_candidates:
    print(
        f"\nREGION {candidate['region_index']}"
    )

    for column in candidate["columns"]:
        print(
            f"  X={column['center_x']:.1f} "
            f"OCC={column['occurrences']}"
        )

print("\nTABLE SUBREGIONS")

for candidate in table_candidates:
    region_index = candidate["region_index"]
    region = candidate["region"]
    columns = candidate["columns"]

    subregions = detect_table_subregions(
        region,
        columns
    )
    for line_index, line in enumerate(region):
        matches = line_matches_columns(
            line,
            columns
        )

        print(
            f"    LINE {line_index}: "
            f"Y={line['center_y']:.1f} "
            f"MATCHES={matches} "
            f"TEXT={' | '.join(item['text'] for item in line['items'])}"
        )
    print(f"\nREGION {region_index}")

    for subregion in subregions:
        print(
            f"  TABLE: "
            f"Y={subregion['top']:.1f} "
            f"to "
            f"{subregion['bottom']:.1f}"
        )


for line_index, line in enumerate(region, start=0):
    matches = line_matches_columns(line, columns)
    width = get_line_width(line)

    print(
        f"    LINE {line_index}: "
        f"Y={line['center_y']:.1f} "
        f"MATCHES={matches} "
        f"ITEMS={len(line['items'])} "
        f"WIDTH={width:.1f} "
        f"TEXT={' | '.join(item['text'] for item in line['items'])}"
    )                                           