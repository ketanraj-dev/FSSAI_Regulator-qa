# FSSAI Food Additives Regulations Q&A Chatbot 🤖

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Powered by LangChain](https://img.shields.io/badge/Powered%20by-LangChain-green.svg)](https://langchain.com/)
[![Powered by OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991.svg)](https://openai.com/)

An intelligent chatbot that provides expert guidance on FSSAI (Food Safety and Standards Authority of India) food additives regulations. Built with LangChain, OpenAI GPT, and Gradio for an interactive web interface.

## 🌟 Features

- **Expert Knowledge**: Trained on official FSSAI food additives regulations document (Compendium_Food_Additives_Regulations_20_12_2022.pdf)
- **RAG Architecture**: Uses Retrieval-Augmented Generation for accurate, document-grounded responses
- **Interactive Web Interface**: Clean and user-friendly Gradio-based chat interface
- **Real-time Responses**: Powered by OpenAI's GPT models for natural language understanding
- **Table Extraction**: Advanced PDF processing that captures both text and tabular data
- **Vector Search**: FAISS-powered semantic search for relevant information retrieval

## 🎯 Use Cases

- Food industry professionals seeking regulatory compliance information
- Food technologists researching permitted additives
- Regulatory affairs specialists needing quick reference
- Students studying food science and regulations
- Anyone with questions about food additive safety and permissions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/ketanraj-dev/FSSAI_Regulator-qa.git
cd FSSAI_Regulator-qa
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up your environment:**
```bash
# Create a .env file in the project root
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```

4. **Process the documents and create vector store:**
```bash
python ingest.py
```

5. **Launch the chatbot:**
```bash
python app.py
```

The web interface will open automatically in your browser at `http://localhost:7860`

## 📋 Project Structure

```
fssai_qa/
├── app.py                  # Main Gradio application
├── ingest.py              # Document processing and vector store creation
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup configuration
├── .env                   # Environment variables (create this)
├── data/
│   └── Compendium_Food_Additives_Regulations_20_12_2022.pdf
├── src/
│   ├── chain_manager.py   # LangChain RAG chain management
│   └── document_processor.py  # PDF processing and chunking
└── vector_store/
    └── faiss_index/       # Generated vector embeddings
```

## 🔧 Configuration

The project uses `config.py` for centralized configuration:

- **Model Settings**: OpenAI model selection and parameters
- **Document Processing**: Chunk size and overlap settings
- **File Paths**: Data and vector store locations
- **System Prompt**: Chatbot behavior customization

## 💡 Example Queries

- "What are the regulations for using Aspartame?"
- "Is Ponceau 4R permitted in any food products?"
- "List the food categories where sorbic acid can be used."
- "What is the maximum permitted level of MSG in processed foods?"
- "Which preservatives are allowed in dairy products?"

## 🛠️ Technical Details

### Architecture

The chatbot follows a Retrieval-Augmented Generation (RAG) architecture:

1. **Document Processing**: PDFs are processed to extract both text and tabular data
2. **Vectorization**: Content is embedded using OpenAI's text-embedding-3-small model
3. **Storage**: Embeddings are stored in FAISS vector database for fast retrieval
4. **Query Processing**: User queries are embedded and matched against the vector store
5. **Response Generation**: Relevant context is provided to GPT for accurate responses

### Key Components

- **LangChain**: Framework for building LLM applications
- **OpenAI GPT**: Language model for natural conversation
- **FAISS**: Vector database for semantic search
- **Gradio**: Web interface framework
- **Camelot**: PDF table extraction
- **PyMuPDF**: PDF text extraction

## 🔒 Environment Variables

Create a `.env` file in the project root with:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 📝 Development

### Running Tests

```bash
python test_debug.py
```

### Installing in Development Mode

```bash
pip install -e .
```

This allows you to use the console commands:
- `run-fssai-ingest` - Process documents
- `run-fssai-chatbot` - Launch the application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FSSAI for providing comprehensive food additives regulations
- OpenAI for powerful language models
- LangChain community for excellent RAG frameworks
- Gradio team for simple web interface creation

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/ketanraj-dev/FSSAI_Regulator-qa/issues) page
2. Create a new issue with detailed information
3. Contact: ketanraj612@gmail.com

## 🔄 Version History

- **v1.0.0** - Initial release with core RAG functionality and Gradio interface

---

**Made with ❤️ for the food industry community**