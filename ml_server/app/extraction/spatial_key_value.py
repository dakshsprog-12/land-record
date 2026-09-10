import re


def get_horizontal_gap(label, value):
    return value["bbox"][0] - label["bbox"][2]


def is_same_line(label, value, y_tolerance=15):
    return abs(
        label["center_y"] - value["center_y"]
    ) <= y_tolerance


def is_to_right(label, value):
    return value["bbox"][0] >= label["bbox"][2]


def looks_like_number(text):
    text = text.strip()

    return bool(
        re.fullmatch(
            r"[\d\s.,₹/-]+",
            text
        )
    )


def looks_like_date_or_year(text):
    text = text.strip()

    if re.fullmatch(r"\d{4}", text):
        return True

    if re.fullmatch(
        r"\d{1,2}[-/]\d{1,2}[-/]\d{2,4}",
        text
    ):
        return True

    if re.fullmatch(
        r"\d{4}-\d{4}",
        text
    ):
        return True

    return False


def looks_like_label(text):
    text = text.strip()

    if not text:
        return False

    if looks_like_number(text):
        return False

    if looks_like_date_or_year(text):
        return False

    return True


def find_spatial_value(label, items, y_tolerance=15, max_gap=80):
    candidates = []

    for item in items:
        if item is label:
            continue

        if not is_same_line(label, item, y_tolerance):
            continue

        if not is_to_right(label, item):
            continue

        gap = get_horizontal_gap(label, item)

        if gap < 0 or gap > max_gap:
            continue

        candidates.append({
            "item": item,
            "gap": gap
        })

    if not candidates:
        return None

    candidates.sort(
        key=lambda candidate: candidate["gap"]
    )

    return candidates[0]


def detect_spatial_key_values(
    regions,
    table_region_indexes=None,
    y_tolerance=15,
    max_gap=80
):
    if table_region_indexes is None:
        table_region_indexes = set()

    candidates = []

    for region_index, region in enumerate(regions, start=1):

        # Skip regions identified as tables.
        if region_index in table_region_indexes:
            continue

        for line in region:
            items = line["items"]

            for label in items:
                label_text = label["text"].strip()

                if not looks_like_label(label_text):
                    continue

                # Inline key-value pairs are handled separately.
                if ":-" in label_text or ":" in label_text:
                    continue

                result = find_spatial_value(
                    label,
                    items,
                    y_tolerance=y_tolerance,
                    max_gap=max_gap
                )

                if result is None:
                    continue

                value = result["item"]

                candidates.append({
                    "label": label_text,
                    "value": value["text"],
                    "label_confidence": label["confidence"],
                    "value_confidence": value["confidence"],
                    "label_bbox": label["bbox"],
                    "value_bbox": value["bbox"],
                    "horizontal_gap": result["gap"],
                    "region_index": region_index
                })

    return candidates