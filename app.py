# app.py
import logging
import gradio as gr
from dotenv import load_dotenv
from src.chain_manager import FssaiChainManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Initializes the chain and launches the Gradio web interface."""
    # Load environment variables (for OPENAI_API_KEY)
    load_dotenv(override=True)
    
    try:
        # Initialize the chain manager which loads the vector store
        chain_manager = FssaiChainManager()
        # Create the conversational chain
        chain = chain_manager.create_chain()

        def chat_stream(user_input, history):
            """Handles the chat interaction by invoking the chain."""
            response = chain.invoke(user_input)
            return response

        # Launch the Gradio Chat Interface
        demo = gr.ChatInterface(
            fn=chat_stream,
            title="FSSAI Food Additives Bot  Regulations Expert 🤖",
            description="Ask me any questions about the FSSAI food additives regulations document.",
            theme="soft",
            examples=[
                ["What are the regulations for using Aspartame?"],
                ["Is Ponceau 4R permitted in any food products?"],
                ["List the food categories where sorbic acid can be used."]
            ]
        )
        demo.launch(inbrowser=True, server_name="0.0.0.0",pwa=True, share=True)

    except FileNotFoundError as e:
        logging.error(e)
        print(f"ERROR: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred. Please check the logs. ERROR: {e}")

if __name__ == "__main__":
    main()