# ActionScribe Local

Offline AI meeting, lecture, and voice-note action extractor built for students, teams, and emerging-market workflows.

## Why this exists

Most productivity AI tools send your private meetings to the cloud.

ActionScribe Local runs offline and turns transcripts into:

- action items
- deadlines
- responsibilities
- summaries

Designed especially for low-bandwidth environments like Pakistan and other emerging regions.

## Features

- Transcript → structured action list
- Deadline detection
- Speaker-aware extraction
- Local-first AI compatible (Ollama / llama.cpp ready)
- Streamlit UI
- CLI mode
- Markdown + JSON export
- Batch processing support

## Quick Start

```bash
pip install -r requirements.txt
python src/cli.py examples/sample.txt
```

Or launch UI:

```bash
streamlit run src/ui.py
```

## Roadmap

- Urdu language support
- WhatsApp chat parser
- PDF ingestion
- Offline RAG integration
- Calendar sync export

## Contributing

PRs welcome. Built for real-world grind outside Silicon Valley.

⭐ Star the repo if it helps your workflow.