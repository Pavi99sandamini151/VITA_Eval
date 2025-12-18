Chatbot with TruLens Evaluation

This project is a FastAPI-based chatbot integrated with TruLens for automated evaluation using the Google Gemini model.

Features

FastAPI chatbot API

TruLens evaluation with:

Relevance

Helpfulness

Gemini model from Google

FastAPI Swagger UI for testing

Optional TruLens dashboard to monitor chatbot evaluation metrics

Prerequisites

Python 3.9+

pip

Virtual environment (venv) recommended

Google Cloud API Key for Gemini (GOOGLE_API_KEY)

Project Structure
vita-final/
│
├── .env                  # Environment variables (GOOGLE_API_KEY)
├── app/
│   ├── main.py           # FastAPI app entry point
│   ├── api/
│   │   └── chat_routes.py  # Chat endpoints
│   ├── chatbot.py        # Your chatbot logic
│   ├── trulens_recorder.py # TruLens integration
│   └── config/
│       └── settings.py   # Load env variables
├── venv/                 # Python virtual environment
└── README.md             # Project documentation

1️⃣ Setup

Clone the repository:

git clone <your-repo-url>
cd vita-final


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate


Install dependencies:

pip install --upgrade pip
pip install -r requirements.txt


Create a .env file in the project root:

GOOGLE_API_KEY=YOUR_GOOGLE_GEMINI_API_KEY


Make sure this is plain text, no quotes or Python code.

2️⃣ Running the App

Start the FastAPI server with hot reload:

python -m uvicorn app.main:app --reload


Default URL: http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

If you want a root endpoint returning JSON, add this to app/main.py:

@app.get("/")
async def root():
    return {"message": "Chatbot API is running"}

3️⃣ Testing the Chatbot
Using Swagger UI

Open http://127.0.0.1:8000/docs in a browser

Find the POST /chat endpoint

Send a JSON request:

{
  "message": "Hello, chatbot!"
}


Response will include your chatbot’s reply evaluated by TruLens.

Using curl
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d "{\"message\": \"Hello\"}"

4️⃣ TruLens Dashboard (optional)

Monitor the evaluation metrics:

venv\Scripts\activate
trulens-dashboard


Open in browser:

http://localhost:8501


See your app (gemini-chatbot-v1)

Track relevance and helpfulness feedback metrics

5️⃣ Notes & Troubleshooting

ValueError: GOOGLE_API_KEY is missing

Ensure .env is in the project root

Restart terminal / uvicorn after editing .env

404 on /

Normal if no root route is defined; use /docs to test

TruLens groundedness error

Groundedness is only available for RAG apps with documents. Remove for plain chat.

Exposed API keys

Rotate any exposed Google API keys immediately

6️⃣ Optional Enhancements

Add thresholds to auto-detect chatbot quality drops

Integrate RAG pipeline for groundedness

Add CI/CD health checks using TruLens feedback

Dockerize the app with environment secrets