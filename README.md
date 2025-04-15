# ScholarGenie 📚

ScholarGenie is a PDF research paper analyzer that uses AI to help researchers and students understand academic papers more easily. It allows users to upload research papers and ask questions about them, providing intelligent responses powered by the Llama3 model and advanced document processing techniques.

## Features ✨

- 📄 Upload and process multiple PDF research papers
- 🤖 AI-powered question answering about paper content
- 🔍 Semantic search across papers
- 💡 Intelligent context understanding
- 🎯 Accurate and relevant responses

## Tech Stack 🛠️

- **Language Model**: Llama3 (via Ollama)
- **Embedding Model**: BAAI/bge-small-en-v1.5
- **Framework**: Streamlit
- **Document Processing**: LlamaIndex, LangChain
- **Vector Store**: FAISS
- **PDF Processing**: PyPDF

## Prerequisites 📋

- Python 3.9+
- Ollama installed with Llama3 model
- Git

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/scholargenie.git
cd scholargenie
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Make sure Ollama is running with Llama3 model:
```bash
ollama run llama3
```

## Usage 💡

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided URL (typically http://localhost:8501)

3. Upload your research papers in PDF format

4. Ask questions about the papers and get AI-powered responses

## Project Structure 📁

```
scholargenie/
├── app.py                 # Main Streamlit application
├── build_index_and_engine.py  # Document processing and indexing
├── papers/               # Directory for PDF papers
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Acknowledgments 🙏

- LlamaIndex team for the amazing document processing framework
- Ollama team for making Llama3 easily accessible
<<<<<<< HEAD
- HuggingFace for the embedding model 
=======
- HuggingFace for the embedding model 
>>>>>>> origin/main
