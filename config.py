# config.py
import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent

# --- File Paths ---
# Source PDF document
PDF_PATH = BASE_DIR / "data" / "Compendium_Food_Additives_Regulations_20_12_2022.pdf"

# Directory to store the FAISS vector index
VECTOR_STORE_PATH = BASE_DIR / "vector_store" / "faiss_index"

# --- Document Processing ---
# Text splitter settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# --- Model Configuration ---
# OpenAI model for embeddings
EMBEDDING_MODEL = "text-embedding-3-small"

# OpenAI model for chat completions
CHAT_MODEL = "gpt-4o-mini"
CHAT_TEMPERATURE = 0.7

# --- Chain & Memory Configuration ---
# Key for conversational memory
MEMORY_KEY = "chat_history"

# System prompt for the chatbot
SYSTEM_PROMPT = """You are an expert in FSSAI food additives regulations.
You must only use the information retrieved from the provided documents.
Do not guess or hallucinate.
If you don’t know the answer, say “The document does not contain this information.” Be gentle and helpful; do not be harsh to the user."""