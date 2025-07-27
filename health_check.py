#!/usr/bin/env python3
"""
Health check script for FSSAI Q&A Chatbot
Run this script to verify your installation is working correctly.
"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if environment is properly configured."""
    print("🔍 Checking environment configuration...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major == 3 and python_version.minor >= 8:
        print(f"✅ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"❌ Python version {python_version.major}.{python_version.minor} is not supported. Please use Python 3.8+")
        return False
    
    # Check for OpenAI API key
    if os.getenv("OPENAI_API_KEY"):
        print("✅ OpenAI API key found")
    else:
        print("❌ OpenAI API key not found. Please set OPENAI_API_KEY in your .env file")
        return False
    
    return True

def check_dependencies():
    """Check if required packages are installed."""
    print("\n📦 Checking dependencies...")
    
    required_packages = [
        'gradio',
        'langchain',
        'langchain_openai',
        'langchain_community',
        'openai',
        'python_dotenv',
        'camelot',
        'fitz',  # PyMuPDF
        'faiss',
        'tiktoken'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'fitz':
                import fitz
            elif package == 'python_dotenv':
                import dotenv
            elif package == 'camelot':
                import camelot
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Install missing packages with: pip install -r requirements.txt")
        return False
    
    return True

def check_project_structure():
    """Check if project files are in place."""
    print("\n📁 Checking project structure...")
    
    required_files = [
        'app.py',
        'ingest.py',
        'config.py',
        'requirements.txt',
        'data/Compendium_Food_Additives_Regulations_20_12_2022.pdf',
        'src/chain_manager.py',
        'src/document_processor.py'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path}")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    
    return True

def check_vector_store():
    """Check if vector store exists."""
    print("\n🗃️ Checking vector store...")
    
    vector_store_path = Path("vector_store/faiss_index")
    
    if vector_store_path.exists() and list(vector_store_path.glob("*")):
        print("✅ Vector store found")
        return True
    else:
        print("⚠️ Vector store not found. Run 'python ingest.py' to create it.")
        return False

def main():
    """Run all health checks."""
    print("🏥 FSSAI Q&A Chatbot Health Check")
    print("=" * 40)
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("⚠️ python-dotenv not installed, skipping .env loading")
    
    checks = [
        check_environment(),
        check_dependencies(),
        check_project_structure(),
        check_vector_store()
    ]
    
    print("\n" + "=" * 40)
    
    if all(checks[:-1]):  # All except vector store check
        print("🎉 Your environment is ready!")
        if not checks[-1]:
            print("📝 Next step: Run 'python ingest.py' to create the vector store")
        else:
            print("🚀 You can now run 'python app.py' to start the chatbot!")
    else:
        print("❌ Please fix the issues above before running the chatbot")
        sys.exit(1)

if __name__ == "__main__":
    main()
