from google import genai
from typing import List, Dict

# ---------------------------
# Gemini configuration
# ---------------------------
# ✅ USE THESE FREE MODELS (from your list):
MODEL_NAME = "models/gemini-2.0-flash"  # FREE and fast!

# Other FREE options you can try:
# MODEL_NAME = "models/gemini-2.5-flash"  # Newer, faster
# MODEL_NAME = "models/gemini-2.0-flash-lite"  # Lightest, fastest
# MODEL_NAME = "models/gemini-2.5-pro"  # Most capable (may have rate limits)

client = genai.Client(api_key=GOOGLE_API_KEY)

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
    try:
        # Build combined prompt using last few turns of history
        prompt_parts = [SYSTEM_PROMPT]

        for msg in chat_history[-5:]:
            prompt_parts.append(f"User: {msg['user']}")
            prompt_parts.append(f"Assistant: {msg['assistant']}")

        prompt_parts.append(f"User: {user_input}")
        contents = "\n".join(prompt_parts)

        # Call Gemini generate_content
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents
        )

        answer = response.text.strip()
        chat_history.append({"user": user_input, "assistant": answer})

        return answer
    
    except Exception as e:
        print(f"Chatbot error: {e}")
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"
