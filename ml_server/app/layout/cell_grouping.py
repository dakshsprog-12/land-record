def merge_continuing_cells(rows, max_vertical_gap=35):
    if not rows:
        return []

    merged_rows = [rows[0]]

    for next_row in rows[1:]:

        previous_row = merged_rows[-1]

        vertical_gap = next_row["y"] - previous_row["y"]

        # Only merge when the rows are very close vertically.
        if vertical_gap <= max_vertical_gap:

            for column_x, items in next_row["columns"].items():

                if column_x in previous_row["columns"]:
                    previous_row["columns"][column_x].extend(items)
                else:
                    previous_row["columns"][column_x] = items

        else:
            merged_rows.append(next_row)

    return merged_rows


def get_item_text(items):
    return " ".join(
        item["text"].strip()
        for item in items
        if item["text"].strip()
    )