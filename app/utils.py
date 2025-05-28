from langdetect import detect

def detect_language(poem):
    lang = detect(poem)
    return "Hindi" if lang == "hi" else "English"

def classify_tone(poem):
    if "death" in poem.lower():
        return "Sad"
    elif "love" in poem.lower():
        return "Romantic"
    elif "nation" in poem.lower():
        return "Patriotic"
    return "Philosophical"