from services.translate import translateNativeToEnglish, translateEnglishToNative

def test_translate_hindi_to_english():
    text = "नमस्ते दुनिया"
    lang = "hi"
    result = translateNativeToEnglish(text, lang)
    assert isinstance(result, str)
    assert "hello" in result.lower() or "world" in result.lower()

def test_translate_english_to_hindi():
    text = "Hello world"
    lang = "hi"
    result = translateEnglishToNative(text, lang)
    assert isinstance(result, str)
    assert "नमस्ते" in result or "दुनिया" in result

