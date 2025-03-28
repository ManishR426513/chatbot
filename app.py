from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from groq_client import GroqClient

app = FastAPI()
templates = Jinja2Templates(directory="templates")
groq_client = GroqClient()

# In-memory chat history
chat_history = []

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "messages": chat_history
    })

@app.post("/chat", response_class=HTMLResponse)
async def post_chat(request: Request, message: str = Form(...)):
    # Add user message to history
    chat_history.append({"role": "user", "content": message})

    # Get response from Groq (filtered by system prompt)
    bot_response = groq_client.get_response(message)
    chat_history.append({"role": "bot", "content": bot_response})

    return templates.TemplateResponse("index.html", {
        "request": request,
        "messages": chat_history
    })