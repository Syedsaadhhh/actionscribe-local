from config import runtime_mode


def call_cloud_model(provider: str, text: str) -> str:
    """
    Placeholder cloud inference router.

    Future:
    integrate OpenAI, Groq, OpenRouter endpoints.
    """
    return f"[Cloud:{provider}] Summary placeholder for: {text[:120]}..."


def call_ollama_model(text: str) -> str:
    """
    Placeholder Ollama inference router.

    Future:
    integrate llama3.2 / phi3 via ollama CLI.
    """
    return f"[Ollama] Summary placeholder for: {text[:120]}..."


def fallback_extract(text: str) -> str:
    """
    Lightweight fallback summarization if no models available.
    """
    sentences = text.split(".")
    return ".".join(sentences[:3])


def generate_summary(text: str) -> str:
    mode_info = runtime_mode()

    if mode_info["mode"] == "cloud":
        return call_cloud_model(mode_info["provider"], text)

    if mode_info["mode"] == "ollama":
        return call_ollama_model(text)

    return fallback_extract(text)


if __name__ == "__main__":
    sample = "Ahmed will prepare slides by Friday. Sara will send the dataset."
    print(generate_summary(sample))
