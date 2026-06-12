# YouTube Video Chatbot using RAG and Ollama

## Overview

This project is a Retrieval-Augmented Generation (RAG) based chatbot that allows users to interact with any YouTube video by asking questions in natural language.

The application extracts the video's transcript, converts it into searchable chunks, stores them in a vector database, and retrieves the most relevant information to answer user queries using a local Large Language Model (LLM).

The entire application runs locally using open-source models and does not require paid APIs.

---

## Aim

To build an intelligent chatbot capable of:

* Extracting transcripts from YouTube videos.
* Understanding the content of the video.
* Answering user questions based solely on the video's transcript.
* Demonstrating an end-to-end RAG pipeline using open-source technologies.
---

## Technologies Used

### Frontend

* Streamlit

### LLM

* Ollama
* Llama 3

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### Vector Database

* FAISS (Facebook AI Similarity Search)

### Framework

* LangChain

### Transcript Extraction

* youtube-transcript-api

### Language

* Python

---

## Project Workflow

1. User enters a YouTube video URL.
2. The application extracts the Video ID.
3. Transcript is fetched using YouTube Transcript API.
4. Transcript is converted into plain text.
5. Text is divided into smaller chunks using Recursive Character Text Splitter.
6. Chunks are converted into vector embeddings.
7. Embeddings are stored inside a FAISS vector database.
8. User asks questions through the chat interface.
9. Retriever fetches the most relevant transcript chunks.
10. Llama 3 generates answers using the retrieved context.
11. Response is displayed in a ChatGPT-like interface.

---

## Architecture

User Question
↓
Retriever (MMR Search)
↓
FAISS Vector Store
↓
Relevant Transcript Chunks
↓
Llama 3 (Ollama)
↓
Final Answer

---

## Features

* Chat with any YouTube video.
* Fully local LLM inference using Ollama.
* Retrieval-Augmented Generation (RAG).
* FAISS-powered semantic search.
* Streamlit-based user interface.
* No dependency on paid LLM APIs.

---

## Future Enhancements

* Support multiple YouTube videos.
* Conversation memory.
* Streaming responses.
* Source citations for retrieved chunks.
* Multi-video knowledge base.
* Agentic AI integration.
* Persistent vector database storage.

---

## Learning Outcomes

Through this project, the following concepts were explored:

* Document Ingestion
* Text Chunking
* Embedding
* Vector Databases
* Semantic Search
* Maximum Marginal Relevance (MMR)
* Retrieval-Augmented Generation (RAG)
* Local LLM Deployment using Ollama
* Streamlit Application Development

---

## Acknowledgement

This project was developed as part of my learning journey in Generative AI and Retrieval-Augmented Generation (RAG).

Special thanks to the CampusX YouTube channel for their high-quality educational content and practical explanations that helped me understand LangChain, RAG pipelines, vector databases, and modern GenAI concepts.

CampusX has been an excellent learning resource for aspiring AI and Machine Learning practitioners.

Thank you to the CampusX team for sharing valuable knowledge with the community.

