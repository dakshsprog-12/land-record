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


def get_line_width(line):
    left = min(
        item["bbox"][0]
        for item in line["items"]
    )

    right = max(
        item["bbox"][2]
        for item in line["items"]
    )

    return right - left


def line_matches_columns(
    line,
    columns,
    x_tolerance=35
):
    matched_columns = set()

    for item in line["items"]:
        item_x = item["center_x"]

        for index, column in enumerate(columns):
            if abs(
                item_x - column["center_x"]
            ) <= x_tolerance:
                matched_columns.add(index)
                break

    return len(matched_columns)


def is_table_like_line(
    line,
    columns,
    x_tolerance=35,
    min_matches=3,
    min_items=2
):
    matches = line_matches_columns(
        line,
        columns,
        x_tolerance
    )

    item_count = len(line["items"])

    return (
        matches >= min_matches
        and item_count >= min_items
    )


def detect_table_subregions(
    region,
    columns,
    x_tolerance=35,
    min_matches=3,
    min_items=3,
    max_gap=45
):
    if not region or not columns:
        return []

    table_lines = []

    for line in region:
        if is_table_like_line(
            line,
            columns,
            x_tolerance=x_tolerance,
            min_matches=min_matches,
            min_items=min_items
        ):
            table_lines.append(line)

    if not table_lines:
        return []

    subregions = []
    current = [table_lines[0]]

    for line in table_lines[1:]:
        previous = current[-1]

        gap = (
            get_line_top(line)
            - get_line_bottom(previous)
        )

        if gap <= max_gap:
            current.append(line)
        else:
            subregions.append(current)
            current = [line]

    subregions.append(current)

    results = []

    for lines in subregions:
        if len(lines) < 2:
            continue

        results.append({
            "top": get_line_top(lines[0]),
            "bottom": get_line_bottom(lines[-1]),
            "lines": lines
        })

    return results