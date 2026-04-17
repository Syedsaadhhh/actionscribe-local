import streamlit as st
from extractor import extract_actions
from summarizer import summarize

st.set_page_config(page_title="ActionScribe Local", layout="wide")

st.title("ActionScribe Local")
st.caption("Offline transcript-to-action intelligence for students and teams")

text = st.text_area("Paste transcript below", height=300)

if st.button("Analyze Transcript"):

    if not text.strip():
        st.warning("Please paste transcript text first.")

    else:
        st.subheader("Summary")
        st.write(summarize(text))

        st.subheader("Action Items")

        actions = extract_actions(text)

        if not actions:
            st.info("No action items detected.")

        for action in actions:
            owner = action.get("owner", "Unknown")
            task = action.get("task", action.get("raw"))
            deadline = action.get("deadline", "unspecified")

            st.markdown(f"**{owner}** → {task} _(deadline: {deadline})_")
