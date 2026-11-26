import os
import gradio as gr

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Select LLM provider and model
MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "genai")
MODEL_NAME = os.getenv("MODEL_NAME", "genimi-3.5-flash-lite")

# Retrieve API key
API_KEYS = {
    "openai": os.getenv("OPENAI_API_KEY"),
    "google_genai": os.getenv("GOOGLE_API_KEY")
}

API_KEY = API_KEYS.get(MODEL_PROVIDER)

if not API_KEY:
    raise ValueError(f"API key for {MODEL_PROVIDER} is missing.")

# Initialize chat model
model = init_chat_model(
    model=MODEL_NAME,
    model_provider=MODEL_PROVIDER,
    api_key=API_KEY,
    temperature=0.4
)

# Define travel personalities
personalities = {
    "Adventure Explorer": """
    You are an adventurous travel guide who specializes in thrilling
    outdoor experiences.

    Recommend destinations for trekking, hiking, camping, wildlife
    exploration, water sports and adventure activities.

    Focus on exciting experiences, natural beauty and outdoor adventures.
    """,

    "Luxury Traveller": """
    You are a premium luxury travel consultant.

    Recommend luxurious destinations, five-star hotels, premium resorts,
    fine dining restaurants, exclusive experiences and comfortable travel.

    Focus on relaxation, elegance and premium experiences.
    """,

    "Budget Backpacker": """
    You are a budget-friendly travel expert.

    Recommend affordable destinations, budget accommodations, hostels,
    street food, public transportation and low-cost activities.

    Focus on helping travellers explore more while spending less.
    """,

    "Cultural Explorer": """
    You are a knowledgeable cultural travel guide.

    Recommend destinations rich in history, culture, architecture,
    museums, local traditions, festivals and authentic cuisine.

    Focus on meaningful cultural experiences and local exploration.
    """
}

EMOJI_STYLE = """
Use relevant emojis to make your answers lively, such as ✈️ 🏖️ 🏔️ 🍜 🏨 💰.
Start each section heading with an emoji. Use at most one per bullet point.
"""


# Travel Guide Assistant function
def travel_guide(question, personality):

    if not question.strip():
        return "Please enter a destination or travel-related question."

    system_prompt = personalities[personality] + EMOJI_STYLE

    try:
        system_msg = SystemMessage(content=system_prompt)

        human_msg = HumanMessage(content=question)

        messages = [system_msg, human_msg]

        response = model.invoke(messages)

        return response.text

    except Exception as e:
        return f"Something went wrong: {str(e)}"


# Create Gradio interface
demo = gr.Interface(
    fn=travel_guide,

    inputs=[
        gr.Textbox(
            lines=4,
            placeholder="Enter your destination place...",
            label="Ask Your Travel Question"
        ),

        gr.Radio(
            choices=list(personalities.keys()),
            value="Adventure Explorer",
            label="Choose Your Travel Personality"
        )
    ],

    outputs=gr.Textbox(
        lines=12,
        label="Your Personalized Travel Recommendations"
    ),

    title="🌍 My Travel Guide Assistant",

    description="""
    Your AI-powered travel companion!

    Choose your travel personality and discover destinations,
    experiences and recommendations tailored to your travel style.
    """
)

# Launch application
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)

