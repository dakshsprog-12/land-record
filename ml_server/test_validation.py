from app.validation.fields import validate_land_record


record = {
    "district": {
        "value": "Rohtas",
        "confidence": 0.96
    },
    "khata_number": {
        "value": "123",
        "confidence": 0.91
    },
    "plot_number": {
        "value": "ABC",
        "confidence": 0.85
    },
    "village": {
        "value": "",
        "confidence": 0.95
    }
}


result = validate_land_record(record)

print(result)