def get_bbox_width(bbox):
    return bbox[2] - bbox[0]


def get_bbox_height(bbox):
    return bbox[3] - bbox[1]


def get_center_x(bbox):
    return (bbox[0] + bbox[2]) / 2


def get_center_y(bbox):
    return (bbox[1] + bbox[3]) / 2


def get_left(bbox):
    return bbox[0]


def get_right(bbox):
    return bbox[2]


def get_top(bbox):
    return bbox[1]


def get_bottom(bbox):
    return bbox[3]


def enrich_line(line):
    """
    Add spatial information to every OCR item in a line.
    """

    for item in line["items"]:
        bbox = item["bbox"]

        item["x"] = get_left(bbox)
        item["y"] = get_top(bbox)

        item["width"] = get_bbox_width(bbox)
        item["height"] = get_bbox_height(bbox)

        item["center_x"] = get_center_x(bbox)
        item["center_y"] = get_center_y(bbox)

    return line


def enrich_lines(lines):

    for line in lines:
        enrich_line(line)

    return lines