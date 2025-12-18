from trulens_eval import Tru, TruCustomApp, Feedback
from google import genai
from app.chatbot import chatbot_response

# Configure Gemini
client = genai.Client(api_key=GOOGLE_API_KEY)
tru = Tru()

# ✅ Use the same model for evaluations
EVAL_MODEL = "models/gemini-2.0-flash"

def relevance_feedback(input_text: str, output_text: str) -> float:
    """Evaluate relevance using FREE Gemini 2.0"""
    try:
        prompt = f"""Rate how relevant this response is to the input on a scale from 0.0 to 1.0.
Only return a single decimal number between 0.0 and 1.0.

Input: {input_text}
Output: {output_text}

Score:"""
        
        response = client.models.generate_content(
            model=EVAL_MODEL,
            contents=prompt
        )
        score = float(response.text.strip())
        return max(0.0, min(1.0, score))
    except Exception as e:
        print(f"Relevance error: {e}")
        return 0.5

def helpfulness_feedback(input_text: str, output_text: str) -> float:
    """Evaluate helpfulness using FREE Gemini 2.0"""
    try:
        prompt = f"""Rate how helpful this response is on a scale from 0.0 to 1.0.
Only return a single decimal number between 0.0 and 1.0.

Input: {input_text}
Output: {output_text}

Score:"""
        
        response = client.models.generate_content(
            model=EVAL_MODEL,
            contents=prompt
        )
        score = float(response.text.strip())
        return max(0.0, min(1.0, score))
    except Exception as e:
        print(f"Helpfulness error: {e}")
        return 0.5

# Create feedback metrics
f_relevance = Feedback(relevance_feedback).on_input_output()
f_helpfulness = Feedback(helpfulness_feedback).on_input_output()

# Wrap chatbot
tru_chatbot = TruCustomApp(
    app=chatbot_response,
    app_id="gemini-chatbot-v1",
    feedbacks=[f_relevance, f_helpfulness]
)

print("✅ TruLens configured with Gemini 2.0 Flash!")
