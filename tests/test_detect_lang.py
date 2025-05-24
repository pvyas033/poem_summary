from app import detect_language

def test_detect_language_english():
    assert detect_language("French") == "en"

def test_detect_language_hindi():
    assert detect_language("नमस्ते") == "fr"
