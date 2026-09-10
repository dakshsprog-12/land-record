def assign_item_to_column(item, columns):
    if not columns:
        return None

    item_x = item["center_x"]

    nearest_column = min(
        columns,
        key=lambda column: abs(item_x - column["center_x"])
    )

    return nearest_column["center_x"]


def build_table_rows(region, columns, x_tolerance=60):
    rows = []

    for line in region:
        row = {}

        for item in line["items"]:
            column_x = assign_item_to_column(item, columns)

            if column_x is None:
                continue

            if abs(item["center_x"] - column_x) > x_tolerance:
                continue

            column_key = f"{column_x:.1f}"

            if column_key not in row:
                row[column_key] = []

            row[column_key].append(item)

        if row:
            rows.append({
                "y": line["center_y"],
                "columns": row
            })

    return rows