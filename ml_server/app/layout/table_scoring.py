def calculate_table_score(region, columns):
    if not region or not columns:
        return 0.0

    row_count = len(region)
    column_count = len(columns)

    if row_count < 2:
        return 0.0

    if column_count < 2:
        return 0.0

    total_items = sum(
        len(line["items"])
        for line in region
    )

    if total_items == 0:
        return 0.0

    # How many OCR items belong to repeated column positions?
    repeated_items = 0

    for line in region:
        for item in line["items"]:
            item_x = item["center_x"]

            for column in columns:
                if abs(item_x - column["center_x"]) <= 35:
                    repeated_items += 1
                    break

    column_coverage = repeated_items / total_items

    # Normalize row count.
    row_score = min(row_count / 10, 1.0)

    # Normalize column count.
    column_score = min(column_count / 6, 1.0)

    score = (
        0.35 * column_score
        + 0.25 * row_score
        + 0.40 * column_coverage
    )

    return round(score, 3)