# app.py
import logging
import gradio as gr
from dotenv import load_dotenv
from src.chain_manager import FssaiChainManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables (for OPENAI_API_KEY)
load_dotenv(override=True)

try:
    # Initialize the chain manager which loads the vector store
    chain_manager = FssaiChainManager()
    # Create the conversational chain
    chain = chain_manager.create_chain()

    def chat_stream(user_input, history):
        """Handles the chat interaction by invoking the chain."""
        response = chain.invoke({"question": user_input})
        return response["answer"]

    # Create the Gradio Interface
    demo = gr.ChatInterface(
        fn=chat_stream,
        title="FSSAI Food Additives Bot 🤖",
        description="Ask me any questions about the FSSAI food additives regulations document.",
        theme="soft",
        examples=[
            ["What are the regulations for using Aspartame?"],
            ["Is Ponceau 4R permitted in any food products?"],
            ["List the food categories where sorbic acid can be used."]
        ]
    )
    
    # Expose the app for Vercel. Use queue() for better performance with multiple users.
    app = demo.queue()

except Exception as e:
    logging.error(f"Failed to initialize the application: {e}")
    # Create a dummy app to show the error on the page if initialization fails
    with gr.Blocks() as app:
        gr.Markdown(f"## 💥 Application Failed to Start\n**Error:** {e}")