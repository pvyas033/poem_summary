from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model_cache = {}

def load_pipeline(task, model_name):
    if model_name not in model_cache:
        tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        model_cache[model_name] = pipeline(task, model= model, tokenizer=tokenizer)
    return model_cache[model_name]