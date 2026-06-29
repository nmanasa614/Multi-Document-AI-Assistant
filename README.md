# 🤖 Multi-Document AI Assistant using Gemini & RAG

A Generative AI-powered Multi-Document Assistant that allows users to upload multiple documents (PDF, DOCX, TXT, and CSV) and ask questions in natural language. The assistant uses Google's Gemini API with Retrieval-Augmented Generation (RAG) to provide accurate answers based on the uploaded documents.

---

## 📌 Project Overview

This project is an AI-powered document question-answering system developed using Python, Streamlit, Google Gemini, LangChain, and ChromaDB.

Instead of answering from general knowledge, the assistant retrieves relevant information from uploaded documents and uses Gemini to generate context-aware responses.

---

## ✨ Features

- 📄 Upload multiple PDF documents
- 📃 Upload DOCX files
- 📝 Upload TXT files
- 📊 Upload CSV files
- 🤖 Gemini AI integration
- 🔍 Retrieval Augmented Generation (RAG)
- 📚 ChromaDB Vector Database
- ✂️ Automatic document chunking
- 🧠 Embedding generation
- 💬 Interactive chat interface
- ⚡ Streamlit Web Application
- 🔐 Secure API Key using .env
- 📂 Modular project structure
- 🚀 Easy deployment

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| Google Gemini | Large Language Model |
| LangChain | AI Framework |
| ChromaDB | Vector Database |
| Google Generative AI Embeddings | Document Embeddings |
| PyPDF | PDF Processing |
| Python-docx | DOCX Processing |
| Pandas | CSV Processing |
| dotenv | Environment Variables |

---

# 📁 Project Structure

```
multi_document_ai/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   ├── uploads/
│   └── chroma_db/
│
├── utils/
│   ├── pdf_loader.py
│   ├── docx_loader.py
│   ├── txt_loader.py
│   ├── csv_loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── rag.py
│   ├── chatbot.py
│   └── memory.py
│
└── assets/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Multi-Document-AI-Assistant.git
```

Go to the project folder

```bash
cd Multi-Document-AI-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure API Key

Create a `.env` file in the project root.

```
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Generate your API key from Google AI Studio:

https://aistudio.google.com/apikey

---

# ▶️ Run the Project

```bash
streamlit run app.py
```

After running, open

```
http://localhost:8501
```

---

# 🚀 How It Works

1. Upload one or more documents.
2. The documents are read and processed.
3. Text is divided into smaller chunks.
4. Embeddings are created for each chunk.
5. Embeddings are stored in ChromaDB.
6. User enters a question.
7. Relevant document chunks are retrieved.
8. Retrieved context is sent to Gemini.
9. Gemini generates an accurate answer.
10. The answer is displayed in the Streamlit interface.

---

# 📸 Application Workflow

```
Upload Documents
        │
        ▼
Read Documents
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store in ChromaDB
        │
        ▼
User Question
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Gemini AI
        │
        ▼
Final Answer
```

---

# 📂 Supported File Types

- PDF
- DOCX
- TXT
- CSV

---

# 📦 Python Packages

- streamlit
- google-genai
- langchain
- langchain-community
- langchain-google-genai
- chromadb
- pypdf
- python-docx
- docx2txt
- pandas
- python-dotenv

---

# 🔮 Future Enhancements

- Conversation Memory
- Voice Assistant
- Image Question Answering
- OCR Support
- Multi-language Support
- Authentication
- Cloud Deployment
- Chat History Database
- Export Chat as PDF
- File Summarization

---

# 🎯 Learning Outcomes

Through this project, you can learn:

- Generative AI
- Retrieval-Augmented Generation (RAG)
- LangChain
- Vector Databases
- Google Gemini API
- Prompt Engineering
- Streamlit Development
- Document Processing
- Embedding Models
- AI Application Development

---

# 👨‍💻 Author

**Manasa**

B.Tech Computer Science Engineering

Generative AI | Python | Data Science

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
