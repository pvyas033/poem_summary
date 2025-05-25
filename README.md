# Poem Summary & Translation Service

A lightweight microservice built with Python and Hugging Face Transformers to:
- Detect language
- Summarize text using LLMs
- Translate between English and native languages (e.g., Hindi)

---

## Features

- **Language Detection** – Detects input language using `langdetect`.
- **Summarization** – Summarizes long texts using pre-trained Transformer models.
- **Translation** – Translates:
  - Native → English
  - English → Native
- **Pluggable Pipelines** – Uses cached transformers via Hugging Face for performance.

---

## Tech Stack

- Python 3.10
- Transformers (HuggingFace)
- Langdetect
- Pytest (for testing)
- GitHub Actions (CI)

---

## Setup

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/poem_summary.git
cd poem_summary
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Running Tests

To run unit tests:
```bash
PYTHONPATH=. pytest tests/
```

Tests are split per function in the `tests/` folder.

---

## Sample API/Use

Here’s how you can use the core functions inside your app:

```python
from services.detect_language import detect_language
from services.summarize import summarize
from services.translate import translateNativeToEnglish
from services.translate import translateEnglishToNative

lang = detect_language("नमस्ते दुनिया")
summary = summarize("Insert a long paragraph here...")
translated = translateNativeToEnglish("नमस्ते दुनिया", "hi")
native_back = translateEnglishToNative("Hello world", "hi")
```

---

> ⚠️ Note: This project is not an agent yet. It's a foundation toward building agentic AI — modular microservices that may later evolve into goal-driven, autonomous systems.


---

## Powered By

- HuggingFace Transformers  
- Helsinki-NLP Translation Models  
- Pytest & GitHub Actions for CI  

---

## Author

**Pankaj Vyas**  
Feel free to contribute, raise issues, or connect!

Email: [pankajvyas033@gmail.com](mailto:pankajvyas033@gmail.com)