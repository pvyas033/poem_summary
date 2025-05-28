from flask import Flask, request, jsonify, render_template

from app import poemagent
from services.detect_language import detect_language
from services.summarize import summarize
from services.translate import translateNativeToEnglish, translateEnglishToNative


poem_summary = Flask(__name__)

@poem_summary.route("/v2/summary-poem", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        poem = request.form.get("poem")
        if poem:
            result = poemagent.invoke({"input": {poem}})
    return result

@poem_summary.route("/v1/summary-poem", methods=["POST"])
def agentic_summary():
    poem = request.json.get('poem')
    if not poem.strip():
        return jsonify({"message": "No poem"})

    lang = detect_language(poem)
    translated = translateNativeToEnglish(poem, lang)
    summary_native = summarize(translated)
    summary_en = translateEnglishToNative(summary_native, lang)

    return jsonify({
        "language-detected": lang,
        "summary-en": summary_en,
        "summary-native": summary_native,
    })

if __name__ == "__main__":
    poem_summary.run(debug=False)