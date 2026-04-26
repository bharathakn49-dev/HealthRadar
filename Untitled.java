import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")


def get_ai_recommendation(outbreak_data):
    prompt = f"""
    You are a Government Public Health AI Officer.

    Analyze the following outbreak data:

    {outbreak_data}

    Give:
    1. Outbreak Severity Score (0–100)
    2. Risk Level (Low / Medium / High)
    3. Why this outbreak is happening
    4. Immediate government actions required
    5. Hospital preparation recommendations
    6. Public awareness recommendations
    7. Final executive summary

    Keep the response professional, concise, and decision-focused.
    """

    response = model.generate_content(prompt)

    return response.text