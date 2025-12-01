"""
Microbots module for the school chatbot system.
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


class SchoolERPBot(Microbot):
    """
    Microbot specialized for Smart School ERP System queries.
    """
    def __init__(self):
        super().__init__(
            "SchoolERPBot",
            ["erp system", "smart school", "school erp", "educational platform", "school management", "digital management platform"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Smart School ERP is a comprehensive digital management platform designed to revolutionize educational institutions. "
            "It integrates all essential school operations including attendance tracking, grade management, timetable scheduling, "
            "fee collection, document management, parent-teacher communication, and administrative workflows into a single, "
            "user-friendly system. Our cloud-based solution ensures seamless access from anywhere, anytime, making school "
            "management efficient and transparent."
        )


class TeacherSupportBot(Microbot):
    """
    Microbot specialized for teacher support queries.
    """
    def __init__(self):
        super().__init__(
            "TeacherSupportBot",
            ["teacher", "teaching", "faculty", "instructor", "educator", "professor", "paperwork", "administrative tasks", "attendance marking", "grade books"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Teachers benefit tremendously through automated attendance marking with biometric integration, digital grade books "
            "with instant report generation, smart timetable management, online assignment submission and grading, student "
            "performance analytics, document issuance capabilities, and direct messaging with parents. The system reduces "
            "paperwork by 80%, saves 2-3 hours daily, and enables teachers to focus more on teaching rather than administrative tasks."
        )


class ParentPortalBot(Microbot):
    """
    Microbot specialized for parent portal queries.
    """
    def __init__(self):
        super().__init__(
            "ParentPortalBot",
            ["parent", "mom", "dad", "guardian", "family", "child", "academic journey", "progress report", "attendance alert", "grade notification"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Parents get comprehensive access to their child's academic journey through real-time attendance alerts, instant "
            "grade notifications, detailed progress reports, fee payment history and online payment options, homework and "
            "assignment tracking, school circulars and announcements, direct communication with teachers, exam schedules "
            "and results, and digital document downloads. Parents receive instant SMS/email notifications for important updates."
        )


class SecurityBot(Microbot):
    """
    Microbot specialized for security-related queries.
    """
    def __init__(self):
        super().__init__(
            "SecurityBot",
            ["security", "secure", "data protection", "privacy", "encryption", "gdpr", "iso 27001", "safe", "audit log"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Security is our top priority. We implement bank-level 256-bit SSL encryption, GDPR-compliant data protection, "
            "regular security audits, role-based access control, secure cloud hosting with automatic backups, two-factor "
            "authentication for admin accounts, and detailed audit logs. Our system is ISO 27001 certified and complies "
            "with educational data privacy regulations. Data is stored in secure, geographically distributed servers."
        )


class CustomizationBot(Microbot):
    """
    Microbot specialized for customization queries.
    """
    def __init__(self):
        super().__init__(
            "CustomizationBot",
            ["custom", "customize", "customization", "specific needs", "unique requirements", "workflow", "philosophy", "grading system", "attendance policy"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Absolutely! Our ERP is highly customizable to match your institution's unique requirements. We can customize "
            "grading systems (GPA, percentage, marks), attendance policies, fee structures and payment plans, report card "
            "formats, timetable templates, curriculum frameworks, examination patterns, and organizational hierarchy. We "
            "work closely with your team to ensure the system aligns perfectly with your existing workflows and educational philosophy."
        )


class SupportTrainingBot(Microbot):
    """
    Microbot specialized for support and training queries.
    """
    def __init__(self):
        super().__init__(
            "SupportTrainingBot",
            ["support", "training", "help", "assistance", "technical support", "webinar", "tutorial", "account manager", "on-site training"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "We offer comprehensive support including 24/7 dedicated support team via phone, email, and chat, on-site "
            "training during implementation, detailed video tutorials and documentation, regular webinars for new features, "
            "dedicated account manager for each school, rapid response time (under 2 hours for critical issues), and annual "
            "system health checks. Our support team understands educational workflows and provides context-aware assistance."
        )


class AttendanceBot(Microbot):
    """
    Microbot specialized for attendance management queries.
    """
    def __init__(self):
        super().__init__(
            "AttendanceBot",
            ["attendance", "present", "absent", "biometric", "rfid", "barcode", "check-in", "absenteeism", "sms alert"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Our attendance system supports multiple methods: biometric integration (face recognition and barcode), RFID card "
            "scanning, mobile app-based check-in, manual marking with geo-location verification, and automated SMS alerts "
            "to parents for absent students. Teachers can mark attendance in under 30 seconds for entire classes, generate "
            "monthly/annual attendance reports, identify patterns of absenteeism, and integrate with leave management systems."
        )


class FinancialManagementBot(Microbot):
    """
    Microbot specialized for financial management queries.
    """
    def __init__(self):
        super().__init__(
            "FinancialManagementBot",
            ["financial", "finance", "fee", "payment", "money", "gst", "budget", "expense", "scholarship", "discount", "payment gateway"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "The system includes comprehensive fee management with customizable fee structures, online payment integration "
            "with multiple payment gateways, automated fee reminders and receipts, scholarship and discount management, "
            "expense tracking and budget planning, financial reporting and analytics, GST compliance for Indian schools, "
            "and multi-campus financial consolidation. Parents can pay fees through UPI, credit cards, net banking, or wallet apps."
        )


class DocumentManagementBot(Microbot):
    """
    Microbot specialized for document management queries.
    """
    def __init__(self):
        super().__init__(
            "DocumentManagementBot",
            ["document", "certificate", "report card", "id card", "admit card", "receipt", "award", "audit trail", "digitally signed"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Our digital document system allows schools to issue and manage student certificates (conduct, transfer, study, "
            "bonafide), mark sheets and report cards, ID cards and admit cards, fee receipts and payment records, achievement "
            "certificates and awards, and other official documents. Documents can be generated automatically, digitally signed, "
            "and shared via email or downloaded. The system maintains a complete audit trail of all issued documents."
        )


class MultiCampusBot(Microbot):
    """
    Microbot specialized for multi-campus queries.
    """
    def __init__(self):
        super().__init__(
            "MultiCampusBot",
            ["campus", "branch", "multiple", "multi-campus", "inter-campus", "centralized", "unified database", "branch-level control"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Yes, our ERP is designed for multi-campus operations. Features include centralized administration with branch-level "
            "controls, unified student database across campuses, inter-campus transfer capabilities, consolidated reporting for "
            "management, branch-specific fee structures and policies, shared resources management, and standardized processes "
            "across all locations while maintaining local autonomy where needed."
        )


class MobileAppBot(Microbot):
    """
    Microbot specialized for mobile app queries.
    """
    def __init__(self):
        super().__init__(
            "MobileAppBot",
            ["mobile", "app", "ios", "android", "push notification", "offline", "gps", "qr code", "smartphone", "photo upload"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Our mobile apps (iOS and Android) provide push notifications for important updates, offline access to timetables "
            "and assignments, QR code-based attendance marking, instant photo/document uploads, GPS-based check-in for staff "
            "and students, real-time chat with teachers and parents, exam result notifications, fee payment processing, and "
            "access to digital ID cards. The apps work seamlessly even with low internet connectivity."
        )


class ExaminationBot(Microbot):
    """
    Microbot specialized for examination and grading queries.
    """
    def __init__(self):
        super().__init__(
            "ExaminationBot",
            ["exam", "examination", "test", "grade", "grading", "mark", "report card", "result", "question paper", "grade analysis"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "The examination module supports multiple exam types (unit tests, mid-terms, finals), customizable grading schemes "
            "and mark distribution, automated report card generation, grade analysis and comparison tools, exam scheduling and "
            "hall allocation, digital question paper management, online examination capabilities, and statistical analysis of "
            "results. Teachers can input grades via mobile or web, and parents receive instant notifications when results are published."
        )


class InfrastructureBot(Microbot):
    """
    Microbot specialized for infrastructure queries.
    """
    def __init__(self):
        super().__init__(
            "InfrastructureBot",
            ["infrastructure", "hardware", "requirement", "server", "internet", "biometric", "printer", "computer", "cloud-based"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Being cloud-based, minimal infrastructure is needed. Requirements include: basic computers with internet access "
            "for admin staff, optional biometric devices for attendance, barcode/QR printers for ID cards, and stable internet "
            "connection (minimum 2 Mbps). No servers or IT infrastructure is required at your end. The system works on desktop "
            "browsers, tablets, and mobile phones. We handle all maintenance, updates, and security patches."
        )


class PricingBot(Microbot):
    """
    Microbot specialized for pricing queries.
    """
    def __init__(self):
        super().__init__(
            "PricingBot",
            ["price", "pricing", "cost", "fee", "plan", "subscription", "annual", "hidden cost", "transparent", "user account"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "We offer flexible pricing based on student strength and features selected. Plans include: all core modules "
            "(attendance, grades, fees, communication), unlimited user accounts (students, parents, teachers, staff), "
            "mobile apps for all users, regular updates and new features, data backup and security, technical support, and "
            "training. No hidden costs - one transparent annual fee. Custom pricing available for large institutions with special requirements."
        )


class ImplementationBot(Microbot):
    """
    Microbot specialized for implementation queries.
    """
    def __init__(self):
        super().__init__(
            "ImplementationBot",
            ["implementation", "implement", "process", "duration", "week", "migration", "configuration", "training", "onboarding", "go-live"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Implementation typically takes 2-4 weeks depending on school size. Process includes: requirement analysis and "
            "customization planning (3-5 days), data migration from existing systems (5-7 days), system configuration and "
            "testing (7-10 days), user training for staff and teachers (3-5 days), parent onboarding and orientation (2-3 days), "
            "and go-live with support team assistance. We provide a dedicated implementation manager throughout the process."
        )


class IntegrationBot(Microbot):
    """
    Microbot specialized for integration queries.
    """
    def __init__(self):
        super().__init__(
            "IntegrationBot",
            ["integration", "integrate", "existing system", "tally", "quickbooks", "paytm", "api", "gateway", "government portal"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Yes, we support extensive integrations including: biometric attendance devices, accounting software (Tally, "
            "QuickBooks), payment gateways (Paytm, PhonePe, Razorpay), SMS gateways for notifications, email service providers, "
            "government education portals, learning management systems, and HR management software. We also provide API access "
            "for custom integrations with your existing systems."
        )


class ActivitiesBot(Microbot):
    """
    Microbot specialized for school activities and events.
    """
    def __init__(self):
        super().__init__(
            "ActivitiesBot",
            ["activity", "event", "program", "celebration", "outing", "field trip"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Our school organizes various activities and events throughout the year to enhance the learning experience of "
            "students. These include cultural programs, sports events, science fairs, field trips, and other educational "
            "outings that help students develop skills beyond academics."
        )


class AcademicsBot(Microbot):
    """
    Microbot specialized for academic programs.
    """
    def __init__(self):
        super().__init__(
            "AcademicsBot",
            ["academic", "curriculum", "subject", "course", "syllabus", "study"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "We offer comprehensive academic programs covering a wide range of subjects and curricula tailored to meet "
            "educational standards. Our academic framework includes detailed syllabi, structured courses, and innovative "
            "teaching methodologies to ensure holistic development of students."
        )


class StudentsBot(Microbot):
    """
    Microbot specialized for student management.
    """
    def __init__(self):
        super().__init__(
            "StudentsBot",
            ["student", "pupil", "learner", "enrollment", "admission", "scholarship"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Our student management system streamlines enrollment processes, tracks academic progress, manages student "
            "records, and facilitates communication between educators and families. We support comprehensive student "
            "information management from admission to graduation."
        )


class FacultyBot(Microbot):
    """
    Microbot specialized for faculty management.
    """
    def __init__(self):
        super().__init__(
            "FacultyBot",
            ["faculty", "teacher", "professor", "instructor", "staff", "educator"]
        )
    
    def respond(self, message: str) -> str:
        return (
            "Our faculty management system helps educational institutions efficiently manage teacher information, track "
            "professional development, facilitate communication, and optimize resource allocation. The system supports "
            "faculty scheduling, performance evaluation, and professional growth tracking."
        )


# Initialize all microbots
MICROBOTS = [
    SchoolERPBot(),
    TeacherSupportBot(),
    ParentPortalBot(),
    SecurityBot(),
    CustomizationBot(),
    SupportTrainingBot(),
    AttendanceBot(),
    FinancialManagementBot(),
    DocumentManagementBot(),
    MultiCampusBot(),
    MobileAppBot(),
    ExaminationBot(),
    InfrastructureBot(),
    PricingBot(),
    ImplementationBot(),
    IntegrationBot(),
    ActivitiesBot(),
    AcademicsBot(),
    StudentsBot(),
    FacultyBot()
]


def get_relevant_microbot(message: str) -> Microbot:
    """
    Get the most relevant microbot for the given message.
    """
    # Priority order: SchoolERP, TeacherSupport, ParentPortal, Security, Customization, SupportTraining, Attendance, 
    # FinancialManagement, DocumentManagement, MultiCampus, MobileApp, Examination, Infrastructure, Pricing, 
    # Implementation, Integration, Activities, Academics, Students, Faculty
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