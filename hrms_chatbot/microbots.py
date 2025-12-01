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
        https://hrms.globaltechsoftwaresolutions.cloud/blogs"""


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


class PricingBot(Microbot):
    """
    Microbot specialized for pricing-related queries.
    """
    def __init__(self):
        super().__init__("PricingBot", [
            "price", "cost", "pricing", "plan", "subscription", 
            "monthly", "annual", "fee", "charge", "budget"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide pricing information.
        """
        return """💰 HRMS Pricing Plans:
        
        🎯 Startup Plan - ₹999/month
        • Up to 50 employees
        • Basic employee management
        • Attendance tracking
        • Payroll processing
        
        🏢 Business Plan - ₹2,499/month
        • Up to 200 employees
        • All Startup features
        • Advanced analytics
        • Custom reports
        • Priority support
        
        🏢 Enterprise Plan - Custom Pricing
        • Unlimited employees
        • All Business features
        • Dedicated account manager
        • Custom integrations
        • 24/7 premium support
        
        💡 Annual plans offer 20% discount!
        Contact our sales team for a personalized quote."""


class ImplementationBot(Microbot):
    """
    Microbot specialized for implementation-related queries.
    """
    def __init__(self):
        super().__init__("ImplementationBot", [
            "implement", "implementation", "deploy", "setup", "install",
            "onboard", "migration", "data transfer", "go live"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide implementation information.
        """
        return """🚀 HRMS Implementation Process:
        
        1. 📋 Discovery & Planning (1-2 weeks)
        • Requirements gathering
        • System configuration planning
        • Timeline establishment
        
        2. 🛠️ System Setup (2-3 weeks)
        • Software installation
        • Customization based on requirements
        • User role configuration
        
        3. 📤 Data Migration (1-2 weeks)
        • Employee data import
        • Historical records transfer
        • Data validation & cleanup
        
        4. 🎓 Training (1 week)
        • Admin training sessions
        • End-user workshops
        • Training materials provided
        
        5. 🚀 Go-Live & Support (Ongoing)
        • System activation
        • Post-go-live support
        • Performance monitoring
        
        Total implementation time: 5-8 weeks depending on organization size."""


class SecurityBot(Microbot):
    """
    Microbot specialized for security-related queries.
    """
    def __init__(self):
        super().__init__("SecurityBot", [
            "security", "secure", "encryption", "privacy", "compliance",
            "gdpr", "data protection", "access control", "authentication"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide security information.
        """
        return """🔒 HRMS Security Features:
        
        🔐 Data Protection
        • AES-256 encryption for data at rest
        • TLS 1.3 encryption for data in transit
        • Regular security audits & penetration testing
        
        👤 Access Control
        • Role-based access control (RBAC)
        • Multi-factor authentication (MFA)
        • Single sign-on (SSO) integration
        
        📜 Compliance
        • GDPR compliant
        • ISO 27001 certified
        • SOC 2 Type II compliant
        
        🛡️ Infrastructure Security
        • AWS cloud infrastructure
        • Regular backups with 99.99% uptime
        • Disaster recovery protocols
        
        🔍 Monitoring
        • 24/7 security monitoring
        • Intrusion detection systems
        • Audit logs for all activities
        
        Your employee data is protected with enterprise-grade security measures."""


class IntegrationBot(Microbot):
    """
    Microbot specialized for integration-related queries.
    """
    def __init__(self):
        super().__init__("IntegrationBot", [
            "integration", "integrate", "api", "third party", "connect",
            "slack", "google", "microsoft", "erp", "accounting", "biometric"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide integration information.
        """
        return """🔗 HRMS Integration Capabilities:
        
        💼 Productivity Tools
        • Slack - Real-time notifications & approvals
        • Microsoft Teams - Seamless collaboration
        • Google Workspace - Single sign-on & document sharing
        
        💰 Accounting Systems
        • QuickBooks - Automated payroll sync
        • Xero - Expense & invoice management
        • Tally - Indian accounting compliance
        
        📊 Analytics & Reporting
        • Power BI - Advanced dashboards
        • Tableau - Custom visualizations
        • Google Analytics - Website recruitment tracking
        
        🔧 Development Tools
        • RESTful API for custom integrations
        • Webhooks for real-time data sync
        • Zapier integration for automation workflows
        
        🔄 Data Sync
        • Bi-directional data synchronization
        • Scheduled automated imports/exports
        • Error handling & retry mechanisms
        
        Our API-first approach ensures seamless integration with your existing tech stack."""


class CustomizationBot(Microbot):
    """
    Microbot specialized for customization-related queries.
    """
    def __init__(self):
        super().__init__("CustomizationBot", [
            "custom", "customize", "customizable", "branding", "workflow",
            "policy", "configuration", "personalize"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide customization information.
        """
        return """🎨 HRMS Customization Options:
        
        🎯 Brand Personalization
        • Company logo and color schemes
        • Custom email templates
        • Branded employee portals
        
        🔄 Workflow Configuration
        • Approval hierarchies
        • Notification preferences
        • Automated processes
        
        📋 Policy Management
        • Leave policies
        • Attendance rules
        • Payroll structures
        
        🛠️ Feature Customization
        • Module selection
        • Field configurations
        • Report customization
        
        Our system is designed to adapt to your organization's unique needs and processes."""


class TrialBot(Microbot):
    """
    Microbot specialized for trial-related queries.
    """
    def __init__(self):
        super().__init__("TrialBot", [
            "trial", "demo", "free", "test", "evaluate", "try"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide trial information.
        """
        return """🆓 HRMS Free Trial:
        
        🕒 Duration: 2-day full access
        • Experience all features
        • No credit card required
        • Dedicated setup assistance
        
        🎯 What You'll Get:
        • Full system access
        • Sample data pre-loaded
        • Guided walkthrough
        • Personalized demo
        
        🚀 Getting Started:
        1. Visit our website
        2. Click 'Start Free Trial'
        3. Complete registration
        4. Receive instant access
        
        Our team will contact you to schedule a personalized demo during your trial period."""


class UpdatesBot(Microbot):
    """
    Microbot specialized for system updates information.
    """
    def __init__(self):
        super().__init__("UpdatesBot", [
            "update", "upgrade", "version", "release", "patch", "improvement"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide system updates information.
        """
        return """🔄 HRMS System Updates:
        
        📅 Update Schedule:
        • Minor updates: Every 6 months
        • Security patches: As needed
        • Major releases: Quarterly
        
        🆕 Update Benefits:
        • New features & enhancements
        • Security improvements
        • Performance optimizations
        • Bug fixes
        
        🛡️ Update Process:
        • Automated deployment
        • Zero downtime upgrades
        • Rollback capability
        • Pre-update notifications
        
        All updates are thoroughly tested before release to ensure system stability."""


class SelfServiceBot(Microbot):
    """
    Microbot specialized for employee self-service features.
    """
    def __init__(self):
        super().__init__("SelfServiceBot", [
            "self-service", "employee portal", "payslip", "leave balance", 
            "attendance record", "document", "profile"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide employee self-service information.
        """
        return """📱 Employee Self-Service Portal:
        
        📄 Personal Management:
        • View/update profile information
        • Access employment documents
        • Download payslips
        
        ⏰ Time & Attendance:
        • Check attendance records
        • View leave balances
        • Apply for time off
        
        💰 Payroll Access:
        • Monthly payslip downloads
        • Tax documents
        • Reimbursement status
        
        📢 Communication:
        • Company announcements
        • Policy updates
        • Team calendars
        
        Employees enjoy 24/7 access to their HR information from any device."""


# Initialize all microbots
MICROBOTS = [
    CompanyNameBot(),
    HRMSBot(),
    SupportBot(),
    AboutBot(),
    BlogBot(),
    PricingBot(),
    ImplementationBot(),
    SecurityBot(),
    IntegrationBot(),
    CustomizationBot(),
    TrialBot(),
    UpdatesBot(),
    SelfServiceBot()
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