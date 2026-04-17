#!/usr/bin/env bash

set -e

echo "Starting ActionScribe Hybrid setup..."

if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Please install Python 3.10+ first."
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "Checking optional Ollama installation..."

if command -v ollama &> /dev/null
then
    echo "Ollama detected. You can run offline mode."
else
    echo "Ollama not found. Hybrid cloud mode still available."
fi

echo "Setup complete. Launching Streamlit UI..."

streamlit run src/ui.py
