from services.summarize import summarize

def test_summarize_short_text():
    text = ("The Eiffel Tower is one of the most iconic landmarks in Paris, "
            "visited by millions of tourists every year.")
    result = summarize(text)
    assert isinstance(result, str)
    assert len(result.split()) <= 50
