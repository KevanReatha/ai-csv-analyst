import streamlit as st
import pandas as pd
from utils.llm_utils import ask_ollama_summary

st.set_page_config(page_title="AI CSV Analyst", layout="centered")
st.title("📊 AI CSV Analyst (Local)")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    if st.button("🧠 Generate Insight with AI"):
        with st.spinner("Analyzing CSV with local LLM..."):
            summary = ask_ollama_summary(df)
            st.subheader("📝 AI Summary")
            st.markdown(summary)