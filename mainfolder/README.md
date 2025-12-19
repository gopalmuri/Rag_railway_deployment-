# fullstack-rag-document-assistant (AI Document Assistant)

An advanced AI-powered document assistant that leverages Retrieval-Augmented Generation (RAG) to provide grounded, context-aware answers from your uploaded PDF documents. This project combines a robust Django backend with a modern frontend, utilizing state-of-the-art LLMs (Groq Llama 3 / Google Gemini) and efficient vector search (ChromaDB).

## Key Features

*   **Intelligent Document Processing:**
    *   Drag-and-drop support for multiple PDF uploads.
    *   Automatic text extraction, cleaning, and semantic chunking using `spaCy`.
*   **Advanced RAG Pipeline:**
    *   Hybrid retrieval system using **ChromaDB** for vector semantic search and **TF-IDF** for keyword matching.
    *   Uses `sentence-transformers` (all-MiniLM-L6-v2) for high-quality embeddings.
*   **Powerful AI Integration:**
    *   Integrated with **Groq (Llama 3)** and **Google Gemini** for lightning-fast, high-quality responses.
    *   Supports local inference via **Ollama**.
    *   Generates relevant follow-up questions to deepen the conversation.
    *   Provides citations and source tracking for complete transparency.
*   **Modern User Interface:**
    *   Clean, responsive dashboard with dark/light mode support.
    *   Real-time processing status updates.
    *   Chat interface with thinking indicators, copy functionality, and chat export options.
*   **Robust Backend:**
    *   Built on **Django Frameork**.
    *   **MySQL** database integration for reliable data management.
    *   Comprehensive logging of ingestion times and system performance.

## Tech Stack

*   **Backend Framework:** Django
*   **Database:** MySQL (Metadata), ChromaDB (Vector Store)
*   **AI/ML:**
    *   **LLMs:** Groq API (Llama 3), Google Gemini API, Ollama (Local)
    *   **Embeddings:** Sentence Transformers
    *   **NLP:** spaCy, NLTK
*   **Frontend:** HTML5, CSS3, JavaScript (Django Templates)
*   **PDF Processing:** PyMuPDF, pdfplumber

## Prerequisites

*   **Python 3.8+**
*   **MySQL Server** (Ensure it is running and a database is created)
*   **API Keys:**
    *   Groq API Key (for Llama 3)
    *   Google Gemini API Key (Optional)

## Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/YourUsername/fullstack-rag-document-assistant.git
    cd fullstack-rag-document-assistant
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Navigate to the `mainfolder` directory where `requirements.txt` is located:
    ```bash
    cd AIDocumentAssistantRAG/mainfolder
    pip install -r requirements.txt
    ```

4.  **Download NLP Models**
    ```bash
    python -m spacy download en_core_web_sm
    ```

5.  **Configure Environment Variables**
    Create a `.env` file or set environment variables for your API keys:
    *   `GROQ_API_KEY`
    *   `GOOGLE_API_KEY`
    *   Database configurations (if not using default settings in `settings.py`)

6.  **Database Setup**
    Ensure your MySQL server is running and configured in `rag_project/settings.py`. Then run migrations:
    ```bash
    cd backend
    python manage.py migrate
    ```

7.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

    Access the application at `http://127.0.0.1:8000/`

## Usage

1.  **Upload Documents:** Use the dashboard to upload PDF files. You will see a progress tracking list.
2.  **Ask Questions:** Navigate to the chat interface and ask questions about your documents.
3.  **View Sources:** The AI will provide citations linking back to the specific parts of the PDF used to answer.
4.  **Export Chat:** Save your conversation history as JSON or TXT.

## Project Structure

*   `backend/rag_app.py`: Core RAG logic (Ingestion, Retrieval, LLM Querying).
*   `backend/ragapp/`: Main Django app handling views and templates.
*   `backend/rag_project/`: Django project settings and configuration.
*   `chroma_db/`: Persistent vector database storage.
*   `uploaded_pdfs/`: Storage for uploaded document files.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
