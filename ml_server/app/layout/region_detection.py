def get_line_top(line):
    return min(
        item["bbox"][1]
        for item in line["items"]
    )


def get_line_bottom(line):
    return max(
        item["bbox"][3]
        for item in line["items"]
    )


def get_line_left(line):
    return min(
        item["bbox"][0]
        for item in line["items"]
    )


def get_line_right(line):
    return max(
        item["bbox"][2]
        for item in line["items"]
    )


def get_line_height(line):
    return get_line_bottom(line) - get_line_top(line)


def get_vertical_gap(previous_line, current_line):
    return (
        get_line_top(current_line)
        - get_line_bottom(previous_line)
    )


def detect_regions(
    lines,
    gap_threshold=50
):
    """
    Group nearby lines into spatial regions.

    This does not assume anything about the document format.
    """

    if not lines:
        return []

    regions = []
    current_region = [lines[0]]

    for current_line in lines[1:]:

        previous_line = current_region[-1]

        gap = get_vertical_gap(
            previous_line,
            current_line
        )

        if gap > gap_threshold:
            regions.append(current_region)
            current_region = [current_line]
        else:
            current_region.append(current_line)

    regions.append(current_region)

    return regions