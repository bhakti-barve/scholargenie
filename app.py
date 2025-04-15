import streamlit as st
import os
from build_index_and_engine import load_and_index
from qa_and_summary import query_index, summarize

st.set_page_config(page_title="ScholarGenie", layout="centered")
st.title("📚 ScholarGenie – Your Local AI Research Assistant")

# Create papers directory if it doesn't exist
if not os.path.exists("papers"):
    os.makedirs("papers")

# Step 1: Upload Files
st.header("Step 1: 📄 Upload Research Papers")
uploaded_files = st.file_uploader("Choose PDF files", type=['pdf'], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        # Save the uploaded file to the papers directory
        with open(os.path.join("papers", uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ Saved {uploaded_file.name}")
    
    # Step 2: Index Papers
    st.header("Step 2: 🔍 Index Papers")
    if st.button("Build Index"):
        with st.spinner("Building index using LLaMA 3 via Ollama..."):
            st.session_state.index = load_and_index("papers")
            st.success("✅ Index built successfully!")

# Step 3: Ask Questions (only show if index exists)
if "index" in st.session_state:
    st.header("Step 3: ❓ Ask Questions")
    question = st.text_input("Enter your question about the paper(s)")
    
    if st.button("Ask"):
        response = query_index(st.session_state.index, question)
        st.markdown(f"**Answer:** {response.response}")

    st.subheader("📝 Summarize")
    if st.button("Summarize Papers"):
        summary = summarize(st.session_state.index)
        st.markdown(f"**Summary:** {summary.response}")
