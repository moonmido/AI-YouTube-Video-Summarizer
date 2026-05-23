
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

summarizer = pipeline(
    "text-generation",
    model="facebook/bart-large-cnn"
)

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)

    if match:
        return match.group(1)

    raise ValueError("Invalid YouTube URL")

def get_transcript(video_id):

    ytt_api = YouTubeTranscriptApi()

    # Try multiple languages
    transcript = ytt_api.fetch(
        video_id,
        languages=['en', 'ar']
    )

    full_text = " ".join(
        [snippet.text for snippet in transcript]
    )

    return full_text

def chunk_text(text, chunk_size=500):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(words[i:i + chunk_size])

        chunks.append(chunk)

    return chunks

def summarize_text(chunks):

    summaries = []

    for chunk in chunks:

        summary = summarizer(
            chunk,
            max_length=120,
            min_length=30,
            do_sample=False
        )

        summaries.append(summary[0]["generated_text"])

    return " ".join(summaries)

if __name__ == "__main__":

    url = input("Enter YouTube URL: ")

    try:

        video_id = extract_video_id(url)

        print("\nFetching transcript...")
        transcript = get_transcript(video_id)

        print("Chunking transcript...")
        chunks = chunk_text(transcript)

        print("Generating summary...\n")
        final_summary = summarize_text(chunks)

        print("=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(final_summary)

    except Exception as e:
        print("Error:", e)