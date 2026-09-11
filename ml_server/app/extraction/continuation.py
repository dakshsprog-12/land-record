from app.extraction.label_mapping import normalize_label


def get_left(item):
    return item["bbox"][0]


def get_right(item):
    return item["bbox"][2]


def get_top(item):
    return item["bbox"][1]


def get_bottom(item):
    return item["bbox"][3]


def is_same_column(item, reference, x_tolerance=40):
    return abs(
        get_left(item) - get_left(reference)
    ) <= x_tolerance


def is_next_line(item, reference, max_vertical_gap=30):
    gap = get_top(item) - get_bottom(reference)

    return 0 <= gap <= max_vertical_gap


def is_new_field(item):
    text = item["text"]

    separators = [
        ":-",
        ":",
    ]

    for separator in separators:
        if separator not in text:
            continue

        label = text.split(separator, 1)[0].strip()

        if normalize_label(label) is not None:
            return True

    return False


def find_continuation_items(
    field_item,
    lines,
    max_vertical_gap=30,
    x_tolerance=40
):
    continuations = []

    for line in lines:
        for item in line["items"]:

            if item is field_item:
                continue

            if is_new_field(item):
                continue

            if not is_same_column(
                item,
                field_item,
                x_tolerance
            ):
                continue

            if not is_next_line(
                item,
                field_item,
                max_vertical_gap
            ):
                continue

            continuations.append(item)

    continuations.sort(
        key=lambda item: item["bbox"][1]
    )

    return continuations