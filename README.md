# 🏥 AI Healthcare Chatbot with RAG and Pinecone

An AI-powered healthcare chatbot that provides instant, reliable medical guidance using Retrieval-Augmented Generation (RAG) and Pinecone vector database. Users can describe their symptoms in natural language and receive context-aware responses backed by medical knowledge.

---

## 🚀 Features

- Understands user symptoms via natural language input
- Uses Retrieval-Augmented Generation (RAG) to provide fact-based responses
- Retrieves relevant medical content from Pinecone vector database
- Generates explanations, first-aid suggestions, and next steps
- Built with a clean web interface using Flask

---

## 🎯 Project Purpose

The chatbot was developed to assist users with basic healthcare advice and reduce the initial load on medical professionals. It aims to improve access to trustworthy medical information, especially in regions with limited healthcare infrastructure.

---

## 🧠 Tech Stack

- **Backend**: Python, Flask  
- **NLP & AI**: Google Gemini / OpenAI (LLM), RAG  
- **Vector Search**: Pinecone  
- **Frontend**: HTML, CSS, JavaScript  
- **Other Tools**: REST APIs, JSON, Git

---

## 🔄 How It Works

1. User enters symptoms in natural language.
2. Symptoms are embedded into vectors using an embedding model.
3. Pinecone retrieves relevant medical context based on the vector similarity.
4. RAG architecture combines the retrieved info with the query.
5. The generative model outputs a grounded response.

---

