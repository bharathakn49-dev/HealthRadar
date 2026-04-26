import ollama


def get_ai_recommendation(outbreak_data):
    prompt = f"""
    You are a Government Public Health AI Officer.

    Analyze the following outbreak data:

    {outbreak_data}

    Give:
    1. Outbreak Severity Score
    2. Risk Level
    3. Why outbreak is happening
    4. Immediate government actions
    5. Hospital preparation recommendations
    6. Public awareness recommendations
    7. Final executive summary
    """

    print("Sending prompt to Ollama...")

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("Received response from Ollama!")

    return response["message"]["content"]