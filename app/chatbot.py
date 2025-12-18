from google import genai
from typing import List, Dict
from app.config.settings import GOOGLE_API_KEY

# ---------------------------
# Gemini configuration
# ---------------------------
# Use a valid Gemini model name that supports generate_content
MODEL_NAME = "gemini-1.5-flash"

# Create the client and use models.generate_content
client = genai.Client(api_key=GOOGLE_API_KEY)

# ---------------------------
# System instruction
# ---------------------------
SYSTEM_PROMPT = """
You are a helpful, knowledgeable AI assistant.
- Give clear, structured, and detailed answers.
- Explain step by step when needed.
- Use bullet points or numbered lists where appropriate.
- If the question is unclear, ask a clarification.
- Be concise but informative.
"""

chat_history: List[Dict[str, str]] = []

def chatbot_response(user_input: str) -> str:
    """
    Generate a detailed chatbot response using the Gemini model.
    """

    # Build combined prompt using last few turns of history
    prompt_parts = [SYSTEM_PROMPT]

    for msg in chat_history[-5:]:
        prompt_parts.append(f"User: {msg['user']}")
        prompt_parts.append(f"Assistant: {msg['assistant']}")

    # Append this message
    prompt_parts.append(f"User: {user_input}")

    contents = "\n".join(prompt_parts)

    # Call Gemini generate_content
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents
    )

    answer = response.text.strip()

    # Store history
    chat_history.append({"user": user_input, "assistant": answer})

    return answer
