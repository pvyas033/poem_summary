from transformers import pipeline

_pipeline = pipeline("text2text-generation", model="google/flan-t5-xl", device=0)

def get_pipeline():
    return _pipeline
