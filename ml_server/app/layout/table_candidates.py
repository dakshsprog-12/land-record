from app.layout.table_detection import detect_table_columns
from app.layout.table_scoring import calculate_table_score


def detect_table_candidates(
    regions,
    min_score=0.5
):
    candidates = []

    for region_index, region in enumerate(
        regions,
        start=1
    ):

        columns = detect_table_columns(region)

        score = calculate_table_score(
            region,
            columns
        )

        if score < min_score:
            continue

        candidates.append({
            "region_index": region_index,
            "score": score,
            "rows": len(region),
            "columns": columns,
            "region": region
        })

    return candidates