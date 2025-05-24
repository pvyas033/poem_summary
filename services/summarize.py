import config
from services.pipeline_cache import load_pipeline

summarizer_model = "facebook/bart-large-cnn"

def summarize(text):

    summarizer = load_pipeline("summarization", summarizer_model)
    summary_en = summarizer(text, max_length=config.MAX_LENGTH, min_length=config.MIN_LENGTH, do_sample=False)[0]['summary_text']

    return summary_en