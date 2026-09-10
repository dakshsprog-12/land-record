def get_item_center_x(item):
    return item["center_x"]


def cluster_x_positions(items, x_tolerance=35):
    x_positions = sorted(
        get_item_center_x(item)
        for item in items
    )

    clusters = []

    for x in x_positions:

        matched_cluster = None

        for cluster in clusters:

            if abs(x - cluster["center_x"]) <= x_tolerance:
                matched_cluster = cluster
                break

        if matched_cluster is None:

            clusters.append({
                "center_x": x,
                "positions": [x]
            })

        else:

            matched_cluster["positions"].append(x)

            matched_cluster["center_x"] = (
                sum(matched_cluster["positions"])
                / len(matched_cluster["positions"])
            )

    return clusters


def detect_table_columns(
    region,
    x_tolerance=35,
    min_occurrences=2
):
    items = []

    for line in region:
        items.extend(line["items"])

    clusters = cluster_x_positions(
        items,
        x_tolerance
    )

    columns = []

    for cluster in clusters:

        if len(cluster["positions"]) >= min_occurrences:

            columns.append({
                "center_x": cluster["center_x"],
                "occurrences": len(
                    cluster["positions"]
                )
            })

    columns.sort(
        key=lambda column: column["center_x"]
    )

    return columns