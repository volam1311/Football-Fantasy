import uvicorn
import os 
import fastapi
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
# Load the app
app = fastapi.FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the API key and the chatbot model
API_KEY = os.environ.get("OPENAI_API_KEY")
chatbot = OpenAI(api_key=API_KEY)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = chatbot.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You have a professional knowledge in football and you help other people answering the questions related to football."},
            {"role": "user", "content": request.message}
        ]
    )
    return {"message": response.choices[0].message.content}

