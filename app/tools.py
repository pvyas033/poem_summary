from app.pipeline import _pipeline

def summarize_poem(poem_text):
    summary = _pipeline(poem_text, max_length=150, truncation=True)[0]["generated_text"]
    return summary

def search_poet(query):
    from duckduckgo_search import duckduckgo_search
    results = duckduckgo_search(query + "poem", max_results=1)
    return results[0]['body'] if results else "No info found."