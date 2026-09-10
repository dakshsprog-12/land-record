from app.extraction.land_record import extract_land_record_fields


text = """
भूमि अभिलेख

खाता संख्या: 123
खसरा संख्या: 456/2
प्लॉट नंबर: 789
क्षेत्रफल: 2.5 एकड़
ग्राम: रामपुर
तहसील: कांके
जिला: रांची
"""


result = extract_land_record_fields(text)

print(result)