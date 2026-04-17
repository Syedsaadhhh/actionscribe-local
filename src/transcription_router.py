from config import runtime_mode


def local_transcribe(audio_path: str) -> str:
    return f"[Local transcription placeholder] Processed: {audio_path}"


def cloud_transcribe(audio_path: str, provider: str) -> str:
    return f"[Cloud:{provider}] Transcription placeholder for: {audio_path}"


def transcription_router(audio_path: str) -> str:
    mode = runtime_mode()

    if mode["mode"] == "cloud":
        return cloud_transcribe(audio_path, mode["provider"])

    if mode["mode"] == "ollama":
        return local_transcribe(audio_path)

    return "Fallback mode: please provide transcript text manually."
