"""
Microbots module for the chatbot system.
This module implements specialized microbots that can handle specific types of queries.
"""

import re
from typing import Dict, List, Tuple

class Microbot:
    """
    Base class for all microbots.
    """
    def __init__(self, name: str, keywords: List[str]):
        self.name = name
        self.keywords = keywords
    
    def can_handle(self, message: str) -> bool:
        """
        Check if this microbot can handle the given message.
        """
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in self.keywords)
    
    def respond(self, message: str) -> str:
        """
        Generate a response for the given message.
        """
        raise NotImplementedError("Subclasses must implement respond method")


class HRMSBot(Microbot):
    """
    Microbot specialized for HRMS-related queries.
    """
    def __init__(self):
        super().__init__("HRMSBot", [
            "hrms", "human resource", "employee management", "payroll", 
            "attendance", "leave", "salary", "biometric", "task management"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide information about HRMS features.
        """
        return """Our HRMS (Human Resource Management System) offers comprehensive solutions:
        
        📊 Employee Management
        • Add, update, remove employees
        • Manage roles, departments & salaries
        • Secure storage of employee documents
        
        ⏰ Attendance & Leave
        • Face recognition check-in/check-out
        • Biometric integration
        • Selfie & location-based attendance
        • Automated attendance reports
        • Leave approval workflow
        • Real-time attendance data
        
        💰 Payroll Management
        • Automatic salary calculations
        • Complete payroll solution
        • Digital salary slips (PDF generation)
        • Automated PF, ESI calculation
        • Salary history & deductions
        
        📋 Task Management
        • Assign tasks to employees
        • Track status & progress
        • Daily/weekly reporting
        
        Contact our support team for a personalized demo!"""


class SupportBot(Microbot):
    """
    Microbot specialized for support-related queries.
    """
    def __init__(self):
        super().__init__("SupportBot", [
            "support", "help", "contact", "email", "phone", "issue", 
            "problem", "troubleshoot", "assistance", "global tech software solutions",
            "global tech", "global tech software"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide support contact information.
        """
        return """📧 Support Contact Information:
        
        • Email: hrglobaltechsoftwaresolutions@gmail.com
        • Phone: +91 98442 81875
        • Address: No 10, 4th Floor, Gaduniya Complex, Ramaiah Layout, Vidyaranyapura, Bangalore - 560097
        
        Our support team is available Monday to Friday, 9:00 AM to 6:00 PM IST.
        For urgent issues, please call our helpline number."""


class AboutBot(Microbot):
    """
    Microbot specialized for company information queries.
    """
    def __init__(self):
        super().__init__("AboutBot", [
            "about", "company", "overview", "mission", "vision", 
            "founder", "history", "story"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide company information.
        """
        return """Global Tech Software Solutions - HRMS
        
        Founded in 2025, we are dedicated to revolutionizing human resources management for businesses of all sizes.
        
        Our Mission: To provide intuitive, powerful software solutions that transform how companies manage their most valuable asset - their people.
        
        Core Values:
        ✓ Innovation - Developing forward-thinking solutions
        ✓ Integrity - Building trust through transparency
        ✓ Efficiency - Simplifying complex processes
        
        Leadership Team:
        • Sharan Patil - CEO & Founder (8+ years in HR technology)
        • Mani Bharadwaj - Tech Lead (Expert in scalable platforms)"""


class BlogBot(Microbot):
    """
    Microbot specialized for blog-related queries.
    """
    def __init__(self):
        super().__init__("BlogBot", [
            "blog", "article", "news", "update", "post", "read", "write"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide blog information.
        """
        return """📚 Our Latest Blog Posts:
        
        1. "The Ultimate Guide to HRMS" - Learn how HRMS transforms human resource management
        2. "Benefits of Implementing HRMS" - Discover efficiency and accuracy improvements
        3. "AI Automation in HR" - See how AI streamlines HR tasks
        
        Visit our website to read these articles and more!
        https://globaltechsoftwaresolutions.cloud/blogs"""


class CompanyNameBot(Microbot):
    """
    Microbot specialized for company name queries.
    """
    def __init__(self):
        super().__init__("CompanyNameBot", [
            "global tech software solutions", "global tech", "global tech software"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide company contact information.
        """
        return """🏢 Global Tech Software Solutions - HRMS
        
        📧 Email: hrglobaltechsoftwaresolutions@gmail.com
        📞 Phone: +91 98442 81875
        📍 Address: No 10, 4th Floor, Gaduniya Complex, Ramaiah Layout, Vidyaranyapura, Bangalore - 560097
        
        Our support team is available Monday to Friday, 9:00 AM to 6:00 PM IST.
        For urgent issues, please call our helpline number."""


# Initialize all microbots
MICROBOTS = [
    CompanyNameBot(),
    HRMSBot(),
    SupportBot(),
    AboutBot(),
    BlogBot()
]


def get_relevant_microbot(message: str) -> Microbot:
    """
    Get the most relevant microbot for the given message.
    """
    # Priority order: HRMS, Support, About, Blog
    for bot in MICROBOTS:
        if bot.can_handle(message):
            return bot
    return None  # pyright: ignore[reportReturnType]


def get_microbot_response(message: str) -> str:
    """
    Get response from the most relevant microbot.
    """
    bot = get_relevant_microbot(message)
    if bot:
        return bot.respond(message)
    return None  # pyright: ignore[reportReturnType]