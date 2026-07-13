# AI Video Assistant

AI Video Assistant is an end-to-end meeting intelligence app that turns audio or video input into a polished, searchable summary. It can process a YouTube link or a local media file, transcribe the content, generate a title and summary, extract action items and decisions, and let you ask questions about the meeting through a RAG-based chat experience.

## Features

- Upload or paste a YouTube URL or local media file
- Convert and chunk audio for processing
- Transcribe speech using Whisper or Sarvam-based transcription
- Generate:
  - a professional meeting title
  - a concise summary
  - action items
  - key decisions
  - open questions
- Chat with the transcript using a Retrieval-Augmented Generation (RAG) workflow
- Provide a modern Streamlit-based user interface

## Tech Stack

- Python
- Streamlit
- Whisper
- Sarvam AI transcription
- LangChain + Mistral AI
- Chroma / vector storage
- yt-dlp, pydub, ffmpeg-python

## Project Structure

- app.py — Streamlit web app
- main.py — CLI pipeline entry point
- core/
  - extractor.py — action items, decisions, and questions extraction
  - rag_engine.py — RAG-based Q&A workflow
  - summarizer.py — title and summary generation
  - transcriber.py — transcription logic
  - vector_store.py — vector database helpers
- utils/
  - audio_processor.py — download, convert, and chunk audio
- tests/
  - test_rag_fallback.py — fallback RAG-related tests

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or newer
- FFmpeg installed and available in your system PATH
- API keys for:
  - Mistral AI
  - Sarvam AI (for Hinglish transcription support)

## Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies

### Windows

```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r Requirements.txt
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r Requirements.txt
```

## Environment Variables

Create a .env file in the project root with the following values:

```env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key
WHISPER_MODEL=small
```

## Running the App

### Streamlit Web App

```bash
streamlit run app.py
```

Then open the local URL shown by Streamlit in your browser.

### CLI Version

```bash
python main.py
```

You will be prompted to enter:
- a YouTube URL or local file path
- the transcription language mode (`english` or `hinglish`)

## Usage Workflow

1. Enter a YouTube URL or local video/audio file
2. The app downloads or converts the media
3. Audio is split into manageable chunks
4. Transcription is generated
5. The system produces a title, summary, action items, key decisions, and questions
6. You can ask follow-up questions about the meeting content through the RAG chat flow

## Notes

- For English transcription, the app uses Whisper locally.
- For Hinglish input, the app uses Sarvam AI to transcribe and translate to English.
- Processing may take some time depending on the size of the input and model loading.

## License

This project is intended for educational and demonstration purposes.
