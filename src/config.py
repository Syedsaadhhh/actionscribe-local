import os
import shutil


def detect_cloud_provider():
    if os.getenv("OPENAI_API_KEY"):
        return "openai"
    if os.getenv("GROQ_API_KEY"):
        return "groq"
    if os.getenv("OPENROUTER_API_KEY"):
        return "openrouter"
    return None


def detect_ollama():
    return shutil.which("ollama") is not None


def runtime_mode():
    """
    Determines execution mode automatically.

    Priority order:
    1. Cloud API
    2. Local Ollama
    3. Lightweight fallback
    """

    provider = detect_cloud_provider()

    if provider:
        return {"mode": "cloud", "provider": provider}

    if detect_ollama():
        return {"mode": "ollama", "provider": "local"}

    return {"mode": "lite", "provider": "heuristic"}


if __name__ == "__main__":
    print(runtime_mode())
