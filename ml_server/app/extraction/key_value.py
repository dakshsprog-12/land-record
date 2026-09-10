def split_label_value(text):
    separators = [
        ":-",
        ":",
    ]

    for separator in separators:
        if separator in text:
            label, value = text.split(separator, 1)

            label = label.strip()
            value = value.strip()

            if label and value and value != "-":
                return {
                    "label": label,
                    "value": value,
                    "separator": separator
                }

    return None


def detect_inline_key_values(lines):
    candidates = []

    for line in lines:

        for item in line["items"]:

            result = split_label_value(
                item["text"]
            )

            if result is None:
                continue

            candidates.append({
                "label": result["label"],
                "value": result["value"],
                "separator": result["separator"],
                "confidence": item["confidence"],
                "bbox": item["bbox"],
                "center_x": item["center_x"],
                "center_y": item["center_y"]
            })

    return candidates