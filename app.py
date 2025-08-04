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

        # Create a custom beige theme
        beige_theme = gr.themes.Base(
            primary_hue="amber",
            secondary_hue="orange", 
            neutral_hue="stone",
            spacing_size="md",
            radius_size="md",
            text_size="md"
        ).set(
            # Background colors - beige tones
            body_background_fill="#F5F5DC",  # Classic beige
            body_background_fill_dark="#E6D7C3",  # Darker beige for dark mode

            # Container backgrounds
            background_fill_primary="#FAF0E6",  # Linen (light beige)
            background_fill_primary_dark="#F0E68C",  # Khaki beige
            background_fill_secondary="#FFF8DC",  # Cornsilk
            background_fill_secondary_dark="#DDD6C7",  # Warm grey beige

            # Block/panel backgrounds
            block_background_fill="#FFFACD",  # Lemon chiffon (light beige)
            block_background_fill_dark="#E8D5B7",  # Tan beige

            # Input field styling
            input_background_fill="#FDF5E6",  # Old lace
            input_background_fill_dark="#F2E6D3",  # Light tan
            input_background_fill_focus="#F5F5DC",  # Beige focus
            input_border_color="#D2B48C",  # Tan border
            input_border_color_focus="#CD853F",  # Peru (darker tan)

            # Button styling
            button_primary_background_fill="#DEB887",  # Burlywood
            button_primary_background_fill_hover="#D2B48C",  # Tan hover
            button_primary_background_fill_dark="#CD853F",  # Peru for dark mode
            button_primary_text_color="#8B4513",  # Saddle brown text
            button_primary_text_color_dark="#FFFFFF",  # White text in dark mode

            button_secondary_background_fill="#F5DEB3",  # Wheat
            button_secondary_background_fill_hover="#DEB887",  # Burlywood hover
            button_secondary_border_color="#D2B48C",  # Tan border
            button_secondary_text_color="#8B4513",  # Saddle brown text

            # Text colors
            body_text_color="#654321",  # Dark brown
            body_text_color_dark="#5D4E37",  # Coffee brown
            block_label_text_color="#8B4513",  # Saddle brown
            block_title_text_color="#654321",  # Dark brown

            # Chat specific styling
            chatbot_code_background_color="#FFF8DC",  # Cornsilk for code blocks

            # Borders and shadows
            block_border_color="#D2B48C",  # Tan
            block_border_color_dark="#CD853F",  # Peru
            shadow_drop="0 2px 4px rgba(139, 69, 19, 0.1)",  # Subtle brown shadow

            # Panel backgrounds
            panel_background_fill="#FAEBD7",  # Antique white
            panel_background_fill_dark="#E6D3BC",  # Warm beige
        )

        # Launch the Gradio Chat Interface with beige theme
        demo = gr.ChatInterface(
            fn=chat_stream,
            title="🌾 FSSAI Food Additives Bot - Regulations Expert 🤖",
            description="Ask me any questions about the FSSAI food additives regulations document. Designed with a warm, natural beige theme for comfortable reading.",
            theme=beige_theme,
            examples=[
                ["What are the regulations for using Aspartame?"],
                ["Is Ponceau 4R permitted in any food products?"],
                ["List the food categories where sorbic acid can be used."],
                ["What is the maximum permitted level of MSG in processed foods?"],
                ["Which preservatives are allowed in dairy products?"]
            ],
            # Additional customization
            css="""
            /* Additional beige theme customizations */
            .gradio-container {
                background: linear-gradient(135deg, #F5F5DC 0%, #FAEBD7 100%);
                font-family: 'Georgia', 'Times New Roman', serif;
            }

            /* Chat message styling */
            .message.user {
                background-color: #F5DEB3 !important;
                border-left: 4px solid #DEB887;
            }

            .message.bot {
                background-color: #FFF8DC !important; 
                border-left: 4px solid #D2B48C;
            }

            /* Header styling */
            .gradio-container h1 {
                color: #8B4513;
                text-shadow: 1px 1px 2px rgba(139, 69, 19, 0.1);
            }

            /* Input area styling */
            .input-container {
                background-color: #FAEBD7;
                border-radius: 12px;
                padding: 8px;
            }

            /* Scrollbar styling */
            ::-webkit-scrollbar {
                width: 8px;
            }

            ::-webkit-scrollbar-track {
                background: #F5F5DC;
            }

            ::-webkit-scrollbar-thumb {
                background: #D2B48C;
                border-radius: 4px;
            }

            ::-webkit-scrollbar-thumb:hover {
                background: #CD853F;
            }
            """
        )

        demo.launch(
            inbrowser=True, 
            server_name="0.0.0.0",
            pwa=True, 
            share=True,
            favicon_path=None,  # You can add a custom favicon here
            app_kwargs={"title": "FSSAI Beige Bot"}
        )

    except FileNotFoundError as e:
        logging.error(e)
        print(f"ERROR: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print(f"An unexpected error occurred. Please check the logs. ERROR: {e}")

if __name__ == "__main__":
    main()
