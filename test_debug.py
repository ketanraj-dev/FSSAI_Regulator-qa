#!/usr/bin/env python3
"""Test script to debug the chain manager."""

import logging
import os
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_chain_manager():
    """Test the chain manager to identify issues."""
    load_dotenv(override=True)
    
    # Check API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY not found in environment")
        return
    else:
        print(f"✓ API Key found: {api_key[:8]}...")
    
    # Test imports
    try:
        print("Testing imports...")
        from src.chain_manager import FssaiChainManager
        print("✓ Chain manager import successful")
    except Exception as e:
        print(f"✗ Import error: {e}")
        return
    
    # Test initialization
    try:
        print("Testing chain manager initialization...")
        chain_manager = FssaiChainManager()
        print("✓ Chain manager initialized successfully")
    except Exception as e:
        print(f"✗ Initialization error: {e}")
        return
    
    # Test chain creation
    try:
        print("Testing chain creation...")
        chain = chain_manager.create_chain()
        print("✓ Chain created successfully")
    except Exception as e:
        print(f"✗ Chain creation error: {e}")
        return
    
    # Test simple query
    try:
        print("Testing simple query...")
        response = chain.invoke({"question": "What is this document about?"})
        print(f"✓ Query successful: {response['answer'][:100]}...")
    except Exception as e:
        print(f"✗ Query error: {e}")
        return
    
    print("All tests passed!")

if __name__ == "__main__":
    test_chain_manager()
