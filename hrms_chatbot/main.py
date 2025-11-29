from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from company_logic import is_company_related, fetch_company_info
from microbots import get_microbot_response

class Message(BaseModel):
    message: str

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(data: Message):
    user_msg = data.message

    # First check if a microbot can handle this query
    microbot_response = get_microbot_response(user_msg)
    if microbot_response:
        return {"reply": microbot_response}
    
    # Otherwise check if it's company related and fetch information
    if is_company_related(user_msg):
        # Fetch company information from the most relevant URL
        answer = fetch_company_info(user_msg)
        return {"reply": answer}

    # Otherwise give default message
    return {"reply": "Please contact admin for more details."}

