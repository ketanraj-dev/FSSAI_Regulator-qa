# src/chain_manager.py
import logging
import os
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI  # Corrected import
from langchain_openai import OpenAIEmbeddings  # Corrected import
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_community.vectorstores import FAISS  # Corrected import

import config

class FssaiChainManager:
    """Manages the creation of the conversational retrieval chain."""

    def __init__(self):
        if not os.path.exists(config.VECTOR_STORE_PATH):
            raise FileNotFoundError(
                f"Vector store not found at {config.VECTOR_STORE_PATH}. "
                f"Please run `ingest.py` first to create it."
            )
        self.vector_store = self._load_vector_store()

    def _load_vector_store(self) -> FAISS:
        """Loads the FAISS vector store from the local path."""
        logging.info("Loading vector store...")
        embedding_model = OpenAIEmbeddings(model=config.EMBEDDING_MODEL)
        # allow_dangerous_deserialization is needed for FAISS with langchain>0.1.14
        return FAISS.load_local(
            str(config.VECTOR_STORE_PATH), 
            embedding_model, 
            allow_dangerous_deserialization=True 
        )

# src/chain_manager.py
import logging
import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS

import config

class FssaiChainManager:
    """Manages the creation of the conversational retrieval chain."""

    def __init__(self):
        if not os.path.exists(config.VECTOR_STORE_PATH):
            raise FileNotFoundError(
                f"Vector store not found at {config.VECTOR_STORE_PATH}. "
                f"Please run `ingest.py` first to create it."
            )
        self.vector_store = self._load_vector_store()

    def _load_vector_store(self) -> FAISS:
        """Loads the FAISS vector store from the local path."""
        logging.info("Loading vector store...")
        embedding_model = OpenAIEmbeddings(model=config.EMBEDDING_MODEL)
        # allow_dangerous_deserialization is needed for FAISS with langchain>0.1.14
        return FAISS.load_local(
            str(config.VECTOR_STORE_PATH), 
            embedding_model, 
            allow_dangerous_deserialization=True 
        )

    def create_chain(self):
        """Creates and returns the conversational retrieval chain."""
        logging.info("Creating conversational retrieval chain...")
        
        # 1. Define Prompt Template
        prompt = ChatPromptTemplate.from_messages([
            ("system", config.SYSTEM_PROMPT),
            ("human", "Question: {question}\n\nContext:\n{context}")
        ])
        
        # 2. Instantiate LLM
        llm = ChatOpenAI(
            temperature=config.CHAT_TEMPERATURE, 
            model=config.CHAT_MODEL,
            streaming=True
        )
        
        # 3. Create the retrieval chain using modern LangChain patterns
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        retriever = self.vector_store.as_retriever()
        
        # Create the chain
        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
        )
        
        logging.info("Chain created successfully.")
        return rag_chain