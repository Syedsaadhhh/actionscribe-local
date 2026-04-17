from typing import List


def summarize(text: str, max_sentences: int = 5) -> str:
    """
    Lightweight extractive summarizer.

    Splits text into sentences and returns the first N sentences.
    Designed for offline-first environments where LLMs may not be available.

    Future upgrade:
    Plug into Ollama or llama.cpp for semantic summarization.
    """

    if not text.strip():
        return "No content provided."

    sentences: List[str] = text.replace("\n", " ").split(".")

    cleaned = [s.strip() for s in sentences if s.strip()]

    return ". ".join(cleaned[:max_sentences]) + ("." if cleaned else "")


if __name__ == "__main__":
    sample = "This is a meeting. Ahmed will prepare slides. Sara will send the report."
    print(summarize(sample))
