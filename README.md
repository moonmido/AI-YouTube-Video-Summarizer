# 🎥 AI YouTube Video Summarizer

An AI-powered YouTube video summarizer built with Python, Hugging Face Transformers, and YouTube Transcript API.

This project extracts subtitles/transcripts from a YouTube video and generates an intelligent summary using a Transformer-based NLP model.

---

# ✨ Features

- Extract YouTube video transcripts
- Supports multiple languages (`en`, `ar`, etc.)
- Automatic transcript chunking
- AI-generated summaries using Hugging Face Transformers
- Simple and lightweight
- Beginner-friendly LLM Engineering project

---

# 🧠 Technologies Used

- Python
- Transformers (Hugging Face)
- PyTorch
- YouTube Transcript API

---

# 📂 Project Structure

```bash
youtube-video-summarizer/
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/youtube-video-summarizer.git
cd youtube-video-summarizer
2. Create Virtual Environment (Recommended)
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
📦 requirements.txt
youtube-transcript-api
transformers
torch
sentencepiece
🚀 Usage

Run the application:

python app.py

Then paste a YouTube URL:

Enter YouTube URL:
https://www.youtube.com/watch?v=xxxxxxxxxxx
🧪 Example Output
Fetching transcript...
Chunking transcript...
Generating summary...

============================================================
SUMMARY
============================================================

This video explains how transformers work,
how attention mechanisms function,
and how modern LLMs process language...
🧩 Supported Languages

The application supports videos with:

English subtitles
Arabic subtitles
Auto-generated captions

Example fallback:

languages=['en', 'ar']
🛠️ Main Components
Transcript Extraction

Uses:

YouTubeTranscriptApi

to retrieve subtitles from YouTube videos.

Text Chunking

Long transcripts are split into smaller chunks to fit Transformer token limits.

AI Summarization

Uses:

facebook/bart-large-cnn

for abstractive summarization.

📜 Example Code
Load Model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)
Generate Summary
result = summarizer(
    chunk,
    max_length=120,
    min_length=30,
    do_sample=False
)
🧠 What You Learn From This Project

This project helps you learn:

NLP pipelines
Hugging Face Transformers
Token chunking
Transcript preprocessing
Prompt engineering basics
LLM application architecture
🚀 Future Improvements
Whisper speech-to-text fallback
FastAPI backend
React frontend
RAG (Retrieval-Augmented Generation)
Ask questions about videos
Vector database integration
Multi-video summarization
Export summaries to PDF
🌐 Deployment Ideas

You can deploy this project for free using:

Render
Railway
Hugging Face Spaces
Vercel (frontend)
📚 Useful Resources
Hugging Face Transformers
YouTube Transcript API
PyTorch
OpenAI Whisper
🤝 Contributing

Pull requests are welcome.

If you'd like to improve the project, feel free to fork the repository and submit a PR.

📄 License

MIT License

👨‍💻 Author

BOUTMEDJET Abd elmoudjib

Software Engineering Student | AI & Backend Developer

GitHub:
https://github.com/moonmido

LinkedIn:
https://linkedin.com/in/abdelmoudjib-boutmedjet-0375a0383/


Useful official docs:

- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- :contentReference[oaicite:2]{index=2}
