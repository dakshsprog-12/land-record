import re


def extract_land_record_fields(text):

    fields = {
        "owner_name": None,
        "khata_number": None,
        "khasra_number": None,
        "plot_number": None,
        "area": None,
        "village": None,
        "tehsil": None,
        "district": None,
        "circle": None,
        "halka": None,
        "mouza": None,
        "jamabandi_number": None
    }

    patterns = {

        "district": [
            r"जिला\s*[:\-]?\s*([^\n]+)",
            r"District\s*[:\-]?\s*([^\n]+)"
        ],

        "circle": [
            r"अंचल\s*[:\-]?\s*([^\n]+)",
            r"Circle\s*[:\-]?\s*([^\n]+)"
        ],

        "halka": [
            r"हल्का\s*[:\-]?\s*([^\n]+)",
            r"Halka\s*[:\-]?\s*([^\n]+)"
        ],

        "mouza": [
            r"मौजा\s*[:\-]?\s*([^\n]+)",
            r"Mouza\s*[:\-]?\s*([^\n]+)"
        ],

        "owner_name": [
            r"जमाबंदी\s*रेयत\s*का\s*नाम\s*[:\-]?\s*([^\n]+)",
            r"रेयत\s*का\s*नाम\s*[:\-]?\s*([^\n]+)"
        ],

        "jamabandi_number": [
            r"कंप्यूटरीकृत\s*जमाब[न्दं]ी\s*संख्या\s*[:\-]?\s*(\d+)"
        ],

        "khata_number": [
            r"खाता\s*संख्या\s*[:\-]?\s*(\d+)",
            r"Khata\s*(?:No\.?|Number)?\s*[:\-]?\s*(\d+)"
        ],

        "khasra_number": [
            r"खेसरा\s*[:\-]?\s*([\d\/\-]+)",
            r"खसरा\s*(?:संख्या|नंबर|नं\.?)?\s*[:\-]?\s*([\d\/\-]+)",
            r"Khasra\s*(?:No\.?|Number)?\s*[:\-]?\s*([\d\/\-]+)"
        ],
        "area": []
        # "area": [
        #     r"रकबा\s*\/?\s*डिसमिल\s*[:\-]?\s*([^\n]+)",
        #     r"रकबा\s*[:\-]?\s*([^\n]+)",
        #     r"क्षेत्रफल\s*[:\-]?\s*([^\n]+)"
        # ]
    }

    for field, field_patterns in patterns.items():

        for pattern in field_patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:

                value = match.group(1).strip()

                # Remove trailing separators
                value = value.strip(" :-")

                fields[field] = value

                break

    return fields