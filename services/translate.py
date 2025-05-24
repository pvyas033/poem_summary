from services.pipeline_cache import load_pipeline

translation_models= {
    'hi': 'Helsinki-NLP/opus-mt-hi-en',
}

reverse_translation_models= {
    'hi': 'Helsinki-NLP/opus-mt-en-hi',
}

def translateNativeToEnglish(text, lang):
    if lang != 'en' and lang in translation_models:
        translator = load_pipeline("translation", translation_models[lang])
        translated = translator(text, max_length = 512)[0]['translation_text']
        return translated

    return "can't translate "

def translateEnglishToNative(text, lang):
    if lang != 'en' and lang in reverse_translation_models:
        reverse_translator = load_pipeline("translation", reverse_translation_models[lang])
        nativeText = reverse_translator(text, max_length=512)[0]['translation_text']
        return nativeText
    return "can't translate "
