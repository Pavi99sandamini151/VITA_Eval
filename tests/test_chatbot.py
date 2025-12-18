from app.chatbot import chatbot_response

def test_chatbot():
    response = chatbot_response("What is Docker?")
    assert isinstance(response, str)
