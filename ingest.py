# ingest.py
import logging
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from src.document_processor import DocumentProcessor
import config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Main function to ingest data and create the vector store."""
    load_dotenv(override=True)
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        logging.error("OPENAI_API_KEY environment variable not set.")
        return

    logging.info("Starting data ingestion process...")

    # 1. Process Documents
    processor = DocumentProcessor(pdf_path=config.PDF_PATH)
    chunks = processor.load_and_chunk()

    if not chunks:
        logging.error("No chunks were created. Halting ingestion.")
        return
        
    # 2. Create Embeddings and Vector Store
    try:
        logging.info(f"Creating embeddings using '{config.EMBEDDING_MODEL}'...")
        embedding_model = OpenAIEmbeddings(model=config.EMBEDDING_MODEL)
        
        vector_db = FAISS.from_documents(chunks, embedding_model)
        
        # 3. Save Vector Store
        config.VECTOR_STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
        vector_db.save_local(str(config.VECTOR_STORE_PATH))
        logging.info(f"Vector store saved successfully at: {config.VECTOR_STORE_PATH}")
        
    except Exception as e:
        logging.error(f"An error occurred during embedding or saving the vector store: {e}")

if __name__ == "__main__":
    main()