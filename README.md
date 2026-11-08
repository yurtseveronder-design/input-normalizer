# Input Normalizer

A lightweight, robust input sanitization and security guardrail utility designed for LLM applications, APIs, and RAG pipelines.

## Features
- **Unicode Normalization:** Standardizes text representations (NFKC) to neutralize homoglyph attacks and encoding tricks.
- **Hidden Character Stripping:** Removes zero-width spaces, directional formatting marks, and control codes.
- **Whitespace Collapsing:** Cleans up excessive spacing, tabs, and unneeded newlines.
- **Heuristic Injection Scanning:** Flags potential prompt injections and system-override attempts with audit metadata.

## Installation

```bash
pip install -e .
pip install -e ".[dev]"
```

## Running Tests

```bash
pytest -v
```

### Test Results Output
```text
========================= test session starts =========================
platform win32 -- Python 3.15.2, pytest-9.2.0, pluggy-1.7.0
rootdir: C:\Users\Dell 5400\input-normalizer
configfile: pyproject.toml
testpaths: tests
plugins: cov-7.1.0
collected 3 items

tests\test_normalizer.py ...                                     [100%]

========================== 3 passed in 0.06s ==========================
```
