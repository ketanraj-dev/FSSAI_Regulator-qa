# src/document_processor.py
import logging
from typing import List
import camelot
from langchain_core.documents import Document
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DocumentProcessor:
    """Handles loading, parsing, and chunking of documents."""

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def _extract_tables(self) -> List[Document]:
        """Extracts tables from the PDF using Camelot."""
        logging.info("Extracting tables from PDF...")
        try:
            tables = camelot.read_pdf(str(self.pdf_path), pages="all", flavor="stream", suppress_stdout=True)
            table_docs = [
                Document(
                    page_content=table.df.to_string(index=False, header=True),
                    metadata={"source": f"table_page_{i}"}
                )
                for i, table in enumerate(tables)
            ]
            logging.info(f"Successfully extracted {len(table_docs)} tables.")
            return table_docs
        except Exception as e:
            logging.error(f"Error extracting tables: {e}")
            return []

    def _extract_text(self) -> List[Document]:
        """Extracts text from the PDF using PyMuPDF."""
        logging.info("Extracting text from PDF...")
        try:
            loader = PyMuPDFLoader(str(self.pdf_path))
            text_docs = loader.load()
            logging.info(f"Successfully extracted {len(text_docs)} pages of text.")
            return text_docs
        except Exception as e:
            logging.error(f"Error extracting text: {e}")
            return []

    def load_and_chunk(self) -> List[Document]:
        """Loads all documents, combines them, and splits into chunks."""
        logging.info("Starting document loading and chunking process...")
        table_docs = self._extract_tables()
        text_docs = self._extract_text()
        all_docs = table_docs + text_docs

        if not all_docs:
            logging.error("No documents were extracted. Aborting.")
            return []
            
        splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        chunks = splitter.split_documents(all_docs)
        logging.info(f"Split documents into {len(chunks)} chunks.")
        return chunks