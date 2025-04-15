import streamlit as st
from build_index_and_engine import load_and_index
from qa_and_summary import query_index, summarize

st.set_page_config(page_title="ScholarGenie", layout="centered")
st.title("📚 ScholarGenie – Your Local AI Research Assistant")

st.markdown("💡 Upload your research papers into the `papers/` folder before indexing.")

path = st.text_input("📂 Enter the path to your PDF folder (default: papers)", value="papers")

if st.button("Index Papers"):
    with st.spinner("Building index using LLaMA 3 via Ollama..."):
        st.session_state.index = load_and_index(path)
        st.success("✅ Index built successfully!")

if "index" in st.session_state:
    st.subheader("🔍 Ask a Question")
    question = st.text_input("Enter your question about the paper(s)")
    
    if st.button("Ask"):
        response = query_index(st.session_state.index, question)
        st.markdown(f"**Answer:** {response.response}")

    st.subheader("📝 Summarize")
    if st.button("Summarize Papers"):
        summary = summarize(st.session_state.index)
        st.markdown(f"**Summary:** {summary.response}")
