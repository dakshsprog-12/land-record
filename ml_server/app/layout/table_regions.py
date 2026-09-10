import re


def get_line_top(line):
    return min(item["bbox"][1] for item in line["items"])


def get_line_bottom(line):
    return max(item["bbox"][3] for item in line["items"])


def line_matches_columns(line, columns, x_tolerance=35):
    matched_columns = set()

    for item in line["items"]:
        item_x = item["center_x"]

        for index, column in enumerate(columns):
            if abs(item_x - column["center_x"]) <= x_tolerance:
                matched_columns.add(index)
                break

    return len(matched_columns)


def looks_like_data_line(line):
    text = " ".join(
        item["text"]
        for item in line["items"]
    ).strip()

    if not text:
        return False

    digit_count = sum(
        character.isdigit()
        for character in text
    )

    return digit_count >= 2


def get_line_score(line, columns, x_tolerance=35):
    match_count = line_matches_columns(
        line,
        columns,
        x_tolerance=x_tolerance
    )

    data = looks_like_data_line(line)

    score = 0

    if match_count >= 2:
        score += 1

    if match_count >= 4:
        score += 1

    if data:
        score += 1

    return score


def detect_table_subregions(
    region,
    columns,
    min_score=1,
    min_table_lines=2,
    x_tolerance=35
):
    if not region or not columns:
        return []

    line_scores = []

    for index, line in enumerate(region):

        score = get_line_score(
            line,
            columns,
            x_tolerance=x_tolerance
        )

        line_scores.append({
            "index": index,
            "score": score
        })

    groups = []
    current_group = []

    for item in line_scores:

        if item["score"] >= min_score:

            if current_group:
                previous = current_group[-1]

                if item["index"] != previous["index"] + 1:

                    if len(current_group) >= min_table_lines:
                        groups.append(current_group)

                    current_group = []

            current_group.append(item)

        else:

            if len(current_group) >= min_table_lines:
                groups.append(current_group)

            current_group = []

    if len(current_group) >= min_table_lines:
        groups.append(current_group)

    subregions = []

    for group in groups:

        start_index = group[0]["index"]
        end_index = group[-1]["index"]

        lines = region[start_index:end_index + 1]

        subregions.append({
            "start_index": start_index,
            "end_index": end_index,
            "lines": lines,
            "top": get_line_top(lines[0]),
            "bottom": get_line_bottom(lines[-1])
        })

    return subregions