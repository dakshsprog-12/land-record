from app.extraction.key_value import detect_inline_key_values


lines = [
    {
        "items": [
            {
                "text": "जिला :- Rohtas",
                "confidence": 0.99,
                "bbox": [69, 238, 207, 260],
                "center_x": 138,
                "center_y": 249
            }
        ]
    },
    {
        "items": [
            {
                "text": "अंचल :- Dehri",
                "confidence": 0.98,
                "bbox": [652, 238, 776, 260],
                "center_x": 714,
                "center_y": 249
            }
        ]
    },
    {
        "items": [
            {
                "text": "मौजा :- भडकुरीया",
                "confidence": 0.97,
                "bbox": [649, 268, 794, 291],
                "center_x": 721,
                "center_y": 279
            }
        ]
    }
]

for line in lines:
    print("\nLINE:")
    for item in line["items"]:
        print(item["text"], item["bbox"])

result = detect_inline_key_values(lines)

for item in result:
    print(item)