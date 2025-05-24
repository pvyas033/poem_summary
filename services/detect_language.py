from langdetect import detect

def detect_language(text):
    lang = detect(text)
    return lang