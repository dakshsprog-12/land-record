def get_center_y(bbox):
    return (bbox[1] + bbox[3]) / 2


def get_center_x(bbox):
    return (bbox[0] + bbox[2]) / 2


def group_into_lines(results, y_tolerance=15):
    """
    Group OCR tokens into horizontal lines based on their Y position.

    This is document-format independent.
    """

    sorted_results = sorted(
        results,
        key=lambda item: (
            get_center_y(item["bbox"]),
            item["bbox"][0]
        )
    )

    lines = []

    for item in sorted_results:
        center_y = get_center_y(item["bbox"])

        matched_line = None

        for line in lines:
            if abs(center_y - line["center_y"]) <= y_tolerance:
                matched_line = line
                break

        if matched_line is None:
            lines.append({
                "center_y": center_y,
                "items": [item]
            })
        else:
            matched_line["items"].append(item)

            # Recalculate the average Y position
            matched_line["center_y"] = sum(
                get_center_y(x["bbox"])
                for x in matched_line["items"]
            ) / len(matched_line["items"])

    # Sort tokens inside every line from left → right
    for line in lines:
        line["items"].sort(
            key=lambda item: item["bbox"][0]
        )

    return lines