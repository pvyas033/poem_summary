from services.detect_language import detect_language

def test_detect_language_english():
    assert detect_language("English") == "en"

def test_detect_language_hindi():
    assert detect_language("नमस्ते") == "hi"
