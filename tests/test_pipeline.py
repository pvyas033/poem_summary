from services.pipeline_cache import load_pipeline

def test_load_translation_pipeline():
    pipe = load_pipeline("translation", "Helsinki-NLP/opus-mt-fr-en")
    assert pipe is not None
    result = pipe("Bonjour tout le monde", max_length=40)
    assert isinstance(result, list)
    assert "translation_text" in result[0]
