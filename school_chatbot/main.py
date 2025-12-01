from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from company_logic import is_company_related, fetch_company_info
from microbots import get_microbot_response
# Import scheduler to start background updates
import scheduler

class Message(BaseModel):
    message: str

class ButtonRequest(BaseModel):
    button: str

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
    user_msg = data.message.strip()
    
    # Handle common greetings
    greetings = ["hi", "hello", "hlo", "hey", "good morning", "good afternoon", "good evening"]
    if user_msg.lower() in greetings:
        return {"reply": "Hi, I'm chatbot assistant. How can I help you today?"}
    
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

@app.post("/button")
def button_response(data: ButtonRequest):
    """Handle button click requests for SCHOOL System"""
    button = data.button.lower()
    
    if button == "school system":
        return {"reply": """🏫 SCHOOL Management System
        
Our innovative SCHOOL Management System provides:

📚 Student Information System
• Student profiles and academic records
• Attendance tracking
• Grade management
• Parent communication portal

👨‍🏫 Staff Management
• Teacher profiles and schedules
• Performance evaluation
• Leave management
• Payroll integration

📅 Academic Calendar
• Event scheduling
• Exam timetables
• Holiday management
• Resource allocation

📈 Reporting & Analytics
• Student performance reports
• Attendance analytics
• Financial reports
• Custom dashboard

Contact our SCHOOL team for a demonstration of how we can transform your educational institution!"""}
    
    else:
        return {"reply": "Please select 'SCHOOL System' for more information."}