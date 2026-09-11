LABEL_MAPPING = {
    "landowner_name": [
        "जमाबंदी रेयत का नाम",
        "भूमि मालिक का नाम",
        "भूमि स्वामी का नाम",
        "landowner name",
        "owner name",
        "land owner name",
    ],

    "guardian_name": [
        "अभिभावक का नाम",
        "पिता का नाम",
        "father name",
        "guardian name",
    ],

    "address": [
        "पता",
        "address",
    ],

    "district": [
        "जिला",
        "जिला का नाम",
        "district",
        "district name",
    ],

    "tehsil": [
        "तहसील",
        "तहसील का नाम",
        "tehsil",
        "tehsil name",
    ],

    "village": [
        "ग्राम",
        "गांव",
        "गाँव",
        "village",
        "village name",
    ],

    "police_station": [
        "थाना",
        "थाना का नाम",
        "police station",
        "police station name",
    ],

    "circle": [
        "अंचल",
        "अंचल का नाम",
        "circle",
        "circle name",
    ],

    "halka": [
        "हल्का",
        "halka",
    ],

    "mouza": [
        "मौजा",
        "मौजा का नाम",
        "mouza",
        "mouza name",
    ],

    "survey_number": [
        "सर्वे नंबर",
        "सर्वेक्षण संख्या",
        "survey number",
        "survey no",
    ],

    "khasra_number": [
        "खसरा संख्या",
        "खसरा नंबर",
        "khasra number",
        "khasra no",
    ],

    "khata_number": [
        "खाता संख्या",
        "खाता नंबर",
        "khata number",
        "khata no",
    ],

    "jamabandi_number": [
        "जमाबंदी संख्या",
        "जमाबन्दी संख्या",
        "जमाबंदी नंबर",
        "जमाबन्दी नंबर",
        "jamabandi number",
        "jamabandi no",
    ],
    "current_part": [
        "भाग वर्तमान",
        "वर्तमान भाग",
        "current part",
    ],

    "plot_number": [
        "प्लॉट नंबर",
        "प्लॉट संख्या",
        "plot number",
        "plot no",
    ],

    "plot_area": [
        "क्षेत्रफल",
        "रकबा",
        "भूमि क्षेत्रफल",
        "area",
        "plot area",
    ],

    "land_classification": [
        "भूमि वर्गीकरण",
        "भूमि का प्रकार",
        "land classification",
        "land type",
    ],

    "mutation_number": [
        "म्यूटेशन संख्या",
        "नामांतरण संख्या",
        "mutation number",
        "mutation no",
    ],

    "registration_number": [
        "पंजीकरण संख्या",
        "रजिस्ट्रेशन संख्या",
        "registration number",
        "registration no",
    ],
}


def normalize_label(label):
    normalized = label.strip().lower()

    for canonical_field, labels in LABEL_MAPPING.items():
        for known_label in labels:
            if normalized == known_label.strip().lower():
                return canonical_field

    return None