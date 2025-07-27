# Contributing to FSSAI Food Additives Regulations Q&A Chatbot

Thank you for your interest in contributing to this project! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

1. **Search existing issues** first to see if the bug has already been reported
2. **Create a new issue** with a clear title and description
3. **Include steps to reproduce** the bug
4. **Add relevant logs or screenshots** if applicable

### Suggesting Features

1. **Check existing feature requests** to avoid duplicates
2. **Create a new issue** with the label "enhancement"
3. **Describe the feature** and its benefits clearly
4. **Explain the use case** for the feature

### Development Setup

1. Fork the repository
2. Clone your fork locally
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
5. Set up your `.env` file with your OpenAI API key

### Making Changes

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** with clear, focused commits
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Follow code style** (see below)

### Code Style Guidelines

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Add comments for complex logic

### Testing

- Run the application locally to ensure it works
- Test with different types of queries
- Verify that the vector store creation works properly

### Pull Request Process

1. **Update the README.md** if your changes affect usage
2. **Ensure your PR addresses a single concern**
3. **Write a clear PR description** explaining what and why
4. **Link to relevant issues** using "Fixes #issue-number"
5. **Be responsive to feedback** during code review

### Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Maintain professional communication

## Development Notes

### Project Structure

- `app.py` - Main Gradio application
- `ingest.py` - Document processing pipeline
- `src/chain_manager.py` - RAG chain management
- `src/document_processor.py` - PDF processing utilities
- `config.py` - Centralized configuration

### Key Dependencies

- **LangChain**: RAG framework
- **OpenAI**: Language models and embeddings
- **FAISS**: Vector database
- **Gradio**: Web interface
- **Camelot**: PDF table extraction

### Common Tasks

- **Adding new document types**: Modify `document_processor.py`
- **Changing models**: Update `config.py`
- **UI improvements**: Modify `app.py`
- **Processing pipeline**: Update `ingest.py`

## Questions?

If you have questions about contributing, please:

1. Check this guide first
2. Look at existing issues and PRs
3. Create a new issue with the "question" label
4. Contact: ketanraj612@gmail.com

Thank you for contributing! 🎉
