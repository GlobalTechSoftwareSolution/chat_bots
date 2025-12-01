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


class ServicesBot(Microbot):
    """
    Microbot specialized for company services-related queries.
    """
    def __init__(self):
        super().__init__("ServicesBot", [
            "service", "software", "development", "web", "mobile", 
            "application", "app", "solution", "technology"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide information about company services.
        """
        return """Our company offers comprehensive software development services:
        
        🌐 Web Development
        • Custom web applications
        • E-commerce platforms
        • Content management systems
        • Responsive website design
        
        📱 Mobile App Development
        • Native iOS and Android apps
        • Cross-platform solutions
        • Mobile UI/UX design
        • App maintenance & updates
        
        ☁️ Cloud Solutions
        • Cloud migration services
        • Infrastructure setup & management
        • Scalable cloud architectures
        • Security & compliance
        
        🔧 Technology Expertise
        • Frontend: React, Vue.js, Angular
        • Backend: Node.js, Python, Java
        • Mobile: React Native, Flutter, Swift, Kotlin
        • Databases: MySQL, PostgreSQL, MongoDB
        
        Visit our website to learn more: https://globaltechsoftwaresolutions.com/
        Contact our team for a consultation on your project!"""


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
        
        • Email: tech@globaltechsoftwaresolutions.com
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
        return """Global Tech Software Solutions
        
        Founded in 2025, we are a leading software development company dedicated to delivering innovative technology solutions for businesses worldwide.
        
        Our Mission: To empower businesses with cutting-edge software solutions that drive growth and efficiency.
        
        Core Values:
        ✓ Innovation - Developing forward-thinking solutions
        ✓ Quality - Delivering robust and reliable software
        ✓ Customer Focus - Understanding and meeting client needs
        ✓ Excellence - Striving for the highest standards
        
        Leadership Team:
        • Sharan Patil - CEO & Founder (10+ years in software development)
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
        
        1. "Modern Web Development Trends in 2025" - Explore the latest technologies shaping web development
        2. "Mobile App vs. Web App: Which is Right for Your Business?" - A comprehensive comparison
        3. "Cloud Migration Best Practices" - Essential tips for moving your infrastructure to the cloud
        
        Visit our website to read these articles and more!
        https://globaltechsoftwaresolutions.com/"""


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
        return """🏢 Global Tech Software Solutions
        
        📧 Email: tech@globaltechsoftwaresolutions.com
        📞 Phone: +91 98442 81875
        📍 Address: No 10, 4th Floor, Gaduniya Complex, Ramaiah Layout, Vidyaranyapura, Bangalore - 560097
        
        Our support team is available Monday to Friday, 9:00 AM to 6:00 PM IST.
        For urgent issues, please call our helpline number."""


class SEOBot(Microbot):
    """
    Microbot specialized for SEO services queries.
    """
    def __init__(self):
        super().__init__("SEOBot", [
            "seo", "search engine optimization", "ranking", "visibility", 
            "organic traffic", "keywords", "google ranking"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide SEO services information.
        """
        return """📈 Search Engine Optimization (SEO) Services:
        
        🔍 Comprehensive SEO Strategy
        • Keyword research & analysis
        • On-page optimization
        • Technical SEO auditing
        • Content optimization
        
        📊 Performance Tracking
        • Rank tracking
        • Traffic analysis
        • Conversion rate optimization
        • Monthly performance reports
        
        🎯 Results-Oriented Approach
        • Improved search rankings
        • Increased organic traffic
        • Higher conversion rates
        • Enhanced online visibility
        
        Learn more at: https://globaltechsoftwaresolutions.com/seo"""


class SEMBot(Microbot):
    """
    Microbot specialized for SEM services queries.
    """
    def __init__(self):
        super().__init__("SEMBot", [
            "sem", "search engine marketing", "ppc", "paid advertising", 
            "google ads", "bing ads", "pay per click"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide SEM services information.
        """
        return """广告服务 Search Engine Marketing (SEM) Services:
        
        🎯 Targeted Advertising Campaigns
        • Google Ads management
        • Bing Ads optimization
        • PPC campaign setup
        • Keyword bidding strategies
        
        💰 Cost-Effective Solutions
        • Budget optimization
        • ROI-focused campaigns
        • Click fraud protection
        • Conversion tracking
        
        📈 Performance Analytics
        • Real-time campaign monitoring
        • Detailed performance reports
        • A/B testing
        • Continuous optimization
        
        Learn more at: https://globaltechsoftwaresolutions.com/sem"""


class SocialMediaBot(Microbot):
    """
    Microbot specialized for social media marketing queries.
    """
    def __init__(self):
        super().__init__("SocialMediaBot", [
            "social media", "facebook", "instagram", "linkedin", 
            "twitter", "social marketing", "engagement"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide social media marketing information.
        """
        return """📱 Social Media Marketing Services:
        
        📢 Strategic Social Media Management
        • Platform-specific content creation
        • Community engagement
        • Brand awareness campaigns
        • Influencer partnerships
        
        📈 Growth & Engagement
        • Follower growth strategies
        • Content calendar planning
        • Engagement optimization
        • Viral content creation
        
        📊 Analytics & Reporting
        • Performance tracking
        • Audience insights
        • ROI measurement
        • Monthly progress reports
        
        Learn more at: https://globaltechsoftwaresolutions.com/social-media"""


class ClientsBot(Microbot):
    """
    Microbot specialized for client-related queries.
    """
    def __init__(self):
        super().__init__("ClientsBot", [
            "client", "customer", "clients", "testimonial", "case study"
        ])
    
    def respond(self, message: str) -> str:
        """
        Provide client information.
        """
        return """👥 Our Valued Clients:
        
        We've successfully partnered with businesses across various industries including:
        • E-commerce & Retail
        • Healthcare & Pharmaceuticals
        • Financial Services
        • Education & EdTech
        • Manufacturing & Logistics
        
        🏆 Client Success Stories
        • Increased online visibility by 300%
        • Reduced customer acquisition costs by 40%
        • Improved conversion rates by 60%
        
        🤝 Partnership Benefits
        • Dedicated account managers
        • Transparent communication
        • Regular progress updates
        • 24/7 support
        
        Learn more at: https://globaltechsoftwaresolutions.com/clients"""


# Initialize all microbots
MICROBOTS = [
    CompanyNameBot(),
    ServicesBot(),
    SupportBot(),
    AboutBot(),
    BlogBot(),
    SEOBot(),
    SEMBot(),
    SocialMediaBot(),
    ClientsBot()
]


def get_relevant_microbot(message: str) -> Microbot:
    """
    Get the most relevant microbot for the given message.
    """
    # Priority order: Services, Support, About, Blog
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