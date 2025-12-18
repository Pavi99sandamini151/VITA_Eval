from trulens_eval import Tru
from trulens_eval.tru_custom_app import TruCustomApp
from trulens_eval.feedback import Feedback
from trulens.providers.google import Google
from app.chatbot import chatbot_response
from app.config.settings import GOOGLE_API_KEY

# Initialize TruLens
tru = Tru()

# Google Gemini provider
google_provider = Google(
    model="models/gemini-1.5-flash",
    api_key=GOOGLE_API_KEY
)

# Feedback metrics
f_relevance = Feedback(google_provider.relevance).on_input_output()
f_helpfulness = Feedback(google_provider.helpfulness).on_input_output()

# Wrap chatbot
tru_chatbot = TruCustomApp(
    app=chatbot_response,
    app_id="gemini-chatbot-v1",
    feedbacks=[f_relevance, f_helpfulness]
)
