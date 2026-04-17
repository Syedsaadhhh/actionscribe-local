import streamlit as st
from src.summarizer import summarize
from src.extractor import extract_actions
from src.history_db import init_db, save_record
from src.exporters import export_markdown, export_whatsapp

init_db()

st.set_page_config(page_title="ActionScribe Hybrid", layout="wide")

st.title("ActionScribe Hybrid")
st.caption("Local-first + cloud-optional transcript intelligence")

TAB1, TAB2, TAB3 = st.tabs(["Upload", "History", "Settings"])

with TAB1:
    text = st.text_area("Paste transcript")

    if st.button("Analyze"):
        if text.strip():
            summary = summarize(text)
            actions = extract_actions(text)

            save_record(summary, str(actions))

            st.subheader("Summary")
            st.write(summary)

            st.subheader("Actions")
            for a in actions:
                st.write("-", a)

            st.download_button("Export Markdown", export_markdown(summary, actions), "actions.md")
            st.download_button("Export WhatsApp", export_whatsapp(actions), "actions.txt")

with TAB2:
    st.info("History viewer coming next upgrade wave.")

with TAB3:
    st.info("Model toggle UI coming next upgrade wave.")
