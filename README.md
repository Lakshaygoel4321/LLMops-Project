# 🧠 Medical Research Chatbot using LLM and Pinecone

This is an **LLMOps-powered Medical Research Assistant** that allows users to query a local PDF (e.g., clinical trial, medical research) and get accurate, context-aware responses via a chatbot interface. It utilizes **LangChain**, **Pinecone vector database**, and **Flask** for the backend, and offers a chat UI with **chat history and timestamps**.

---

## 🚀 Features

* 💬 **Chatbot Interface** with timestamps and history
* 📄 **PDF-based knowledge ingestion** (Medical Reports / Trials)
* 🧠 **LLM-powered context retrieval** using LangChain
* 📦 **Vector Store** using Pinecone for scalable semantic search
* 🌐 **Flask Web App** for interactive user interface
* 🎨 Custom **CSS Styling**
* 🧪 Organized trial notebooks for experimentation

---

## 🗂️ Project Structure

```
LLMops-Project/
│
├── data/
│   └── medical.pdf                # Source medical PDF file
│
├── research/
│   └── trial.ipynb               # Jupyter notebook for testing and experimentation
│
├── src/
│   ├── prompt.py                 # Custom prompt templates
│   └── loader.py                 # PDF loading and text splitting logic
│
├── static/
│   └── style.css                 # UI Styling (Chat + Layout)
│
├── templates/
│   └── index.html                # Flask front-end HTML template
│
├── app.py                        # Main Flask application
├── main.py                       # Core logic to initialize components
├── vectore_store_db.py          # Pinecone vector store configuration
├── templates.py                  # Templating and rendering logic
├── setup.py                      # Environment and setup file
└── requirements.txt              # Dependencies list
```

---

## ⚙️ Technologies Used

* **Python**
* **Flask** (Web framework)
* **LangChain** (LLM integration)
* **Pinecone** (Vector database)
* **OpenAI GPT / LLM model**
* **HTML/CSS** (Chat UI)
* **Jupyter Notebook** (for R\&D)

---

## 🧪 How It Works

1. **PDF Ingestion**: The medical PDF is loaded, split into chunks, and converted into embeddings.
2. **Vector Storage**: These embeddings are stored in Pinecone for fast retrieval.
3. **User Query**: The chatbot accepts user queries from a Flask-powered frontend.
4. **Context Retrieval**: LangChain retrieves relevant chunks from Pinecone.
5. **LLM Response**: The context is passed to the LLM to generate an intelligent response.
6. **Display**: The response is shown in the browser along with timestamps.

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/your-username/LLMops-Project.git
cd LLMops-Project

# Create environment (you are using 'uv' so we'll assume pip/conda environment)
pip install -r requirements.txt

# Start the Flask server
python app.py
```

> ⚠️ Make sure you configure your **Pinecone API key** and **OpenAI API key** in a `.env` or config file before running.

---

## ✅ Requirements

* Python 3.9+
* `Flask`
* `langchain`
* `pinecone-client`
* `openai`
* `uvicorn` or local server setup
* `PyMuPDF` or `pdfplumber` for PDF reading (if used)

---

## 📸 Screenshots

*You can add UI screenshots here.*

---

## 📌 Future Improvements

* Add multi-PDF support
* Implement user authentication
* Chat history download/export
* Real-time LLM model switching (OpenAI, Cohere, etc.)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests for improvements or new features.

---

## 📄 License

This project is licensed under the MIT License.

---

Would you like me to generate this as a `.md` file for direct upload to GitHub?
