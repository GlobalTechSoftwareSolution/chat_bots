import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# URL mappings for different sections
BASE_URL = "https://school.globaltechsoftwaresolutions.cloud/"
ABOUT_URL = BASE_URL + "about"
ACTIVITIES_URL = BASE_URL + "activities"
ACADEMICS_URL = BASE_URL + "nav_features/academics"
STUDENTS_URL = BASE_URL + "nav_features/students"
FACULTY_URL = BASE_URL + "nav_features/faculty"
CONTACT_URL = BASE_URL + "contact"

# Default URL for general company info
COMPANY_URL = os.getenv("COMPANY_URL", BASE_URL)

# Crawled URLs cache
CRAWLED_URLS = {}

# Local testing mode
LOCAL_TESTING = os.getenv("LOCAL_TESTING", "false").lower() == "true"
LOCAL_DATA_DIR = os.getenv("LOCAL_DATA_DIR", "./local_data")

# Keywords used to detect if the user is asking about your company
COMPANY_KEYWORDS = [
    "school",
    "education",
    "student",
    "teacher",
    "faculty",
    "academic",
    "learning",
    "institution",
    "management",
    "system",
    "software",
    "erp",
    "attendance",
    "grade",
    "exam",
    "timetable",
    "library",
    "fees",
    "payment",
    "parent",
    "portal",
    "activity",
    "event"
]

# Keywords for specific sections
ABOUT_KEYWORDS = [
    "about",
    "overview",
    "history",
    "mission",
    "vision",
    "team",
    "founder",
    "story",
]

CONTACT_KEYWORDS = [
    "contact",
    "email",
    "phone",
    "address",
    "location",
    "hours",
    "support",
    "call",
    "reach",
]

ACTIVITIES_KEYWORDS = [
    "activity",
    "event",
    "program",
    "function",
    "celebration",
    "outing",
    "field trip"
]

ACADEMICS_KEYWORDS = [
    "academic",
    "curriculum",
    "subject",
    "course",
    "syllabus",
    "study",
    "learning",
    "education"
]

STUDENTS_KEYWORDS = [
    "student",
    "pupil",
    "learner",
    "enrollment",
    "admission",
    "scholarship"
]

FACULTY_KEYWORDS = [
    "faculty",
    "teacher",
    "professor",
    "instructor",
    "staff",
    "educator"
]

BLOGS_KEYWORDS = [
    "blog",
    "article",
    "news",
    "update",
    "post",
    "read",
    "write",
]


def is_company_related(message: str) -> bool:
    """
    Detect if the user message is related to your company
    using simple keyword matching.
    """
    message = message.lower()
    return any(keyword in message for keyword in COMPANY_KEYWORDS)


def crawl_relevant_pages(base_url: str) -> dict:
    """
    Crawl the website to discover relevant pages and their content.
    """
    global CRAWLED_URLS
    
    # If we've already crawled, return cached results
    if CRAWLED_URLS:
        return CRAWLED_URLS
    
    try:
        # Fetch the main page
        response = requests.get(base_url, timeout=10)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all links
        links = soup.find_all('a', href=True)
        
        # Process each link
        for link in links:
            href = str(link['href'])
            # Convert relative URLs to absolute
            absolute_url = urljoin(base_url, href)
            
            # Only process URLs from the same domain
            if urlparse(absolute_url).netloc == urlparse(base_url).netloc:
                # Check if this is a relevant page based on common patterns
                path = urlparse(absolute_url).path.lower()
                if 'about' in path:
                    CRAWLED_URLS['about'] = absolute_url
                elif 'contact' in path:
                    CRAWLED_URLS['contact'] = absolute_url
                elif 'activities' in path or 'events' in path:
                    CRAWLED_URLS['activities'] = absolute_url
                elif 'academics' in path or 'curriculum' in path:
                    CRAWLED_URLS['academics'] = absolute_url
                elif 'students' in path or 'pupils' in path:
                    CRAWLED_URLS['students'] = absolute_url
                elif 'faculty' in path or 'teachers' in path:
                    CRAWLED_URLS['faculty'] = absolute_url
                elif 'blog' in path or 'news' in path:
                    CRAWLED_URLS['blog'] = absolute_url
                elif 'service' in path or 'product' in path:
                    CRAWLED_URLS['service'] = absolute_url
        
        # Set defaults if not found
        if 'about' not in CRAWLED_URLS:
            CRAWLED_URLS['about'] = ABOUT_URL
        if 'contact' not in CRAWLED_URLS:
            CRAWLED_URLS['contact'] = CONTACT_URL
        if 'activities' not in CRAWLED_URLS:
            CRAWLED_URLS['activities'] = ACTIVITIES_URL
        if 'academics' not in CRAWLED_URLS:
            CRAWLED_URLS['academics'] = ACADEMICS_URL
        if 'students' not in CRAWLED_URLS:
            CRAWLED_URLS['students'] = STUDENTS_URL
        if 'faculty' not in CRAWLED_URLS:
            CRAWLED_URLS['faculty'] = FACULTY_URL
        if 'blog' not in CRAWLED_URLS:
            CRAWLED_URLS['blog'] = BASE_URL
        if 'service' not in CRAWLED_URLS:
            CRAWLED_URLS['service'] = BASE_URL
            
        return CRAWLED_URLS
    except Exception as e:
        # Fallback to hardcoded URLs if crawling fails
        CRAWLED_URLS = {
            'about': ABOUT_URL,
            'contact': CONTACT_URL,
            'blog': BLOGS_URL,
            'service': BASE_URL
        }
        return CRAWLED_URLS


def select_relevant_url(message: str) -> str:
    """
    Select the most relevant URL based on the user's message.
    """
    message_lower = message.lower()
    
    # Crawl the website to find relevant pages
    crawled_urls = crawl_relevant_pages(BASE_URL)
    
    # Check for specific section keywords
    if any(keyword in message_lower for keyword in ABOUT_KEYWORDS):
        return crawled_urls.get('about', ABOUT_URL)
    elif any(keyword in message_lower for keyword in CONTACT_KEYWORDS):
        return crawled_urls.get('contact', CONTACT_URL)
    elif any(keyword in message_lower for keyword in ACTIVITIES_KEYWORDS):
        return crawled_urls.get('activities', ACTIVITIES_URL)
    elif any(keyword in message_lower for keyword in ACADEMICS_KEYWORDS):
        return crawled_urls.get('academics', ACADEMICS_URL)
    elif any(keyword in message_lower for keyword in STUDENTS_KEYWORDS):
        return crawled_urls.get('students', STUDENTS_URL)
    elif any(keyword in message_lower for keyword in FACULTY_KEYWORDS):
        return crawled_urls.get('faculty', FACULTY_URL)
    elif any(keyword in message_lower for keyword in BLOGS_KEYWORDS):
        return crawled_urls.get('blog', BASE_URL)
    else:
        # Default to main company URL
        return COMPANY_URL


def fetch_local_content(url: str) -> str:
    """
    Fetch content from local files for testing purposes.
    """
    import os
    
    # Map URLs to local file names
    url_mapping = {
        BASE_URL: "index.html",
        ABOUT_URL: "about.html",
        ACTIVITIES_URL: "activities.html",
        ACADEMICS_URL: "academics.html",
        STUDENTS_URL: "students.html",
        FACULTY_URL: "faculty.html",
        CONTACT_URL: "contact.html"
    }
    
    try:
        # Determine which file to read based on the URL
        file_name = url_mapping.get(url, "index.html")
        file_path = os.path.join(LOCAL_DATA_DIR, file_name)
        
        # Check if file exists
        if not os.path.exists(file_path):
            return f"Local file not found: {file_path}. Please create local test files for testing."
        
        # Read the local HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse HTML content
        soup = BeautifulSoup(content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Extract text content and clean it up
        text_content = soup.get_text()
        
        # Clean up whitespace
        lines = [line.strip() for line in text_content.splitlines()]
        chunks = [phrase for line in lines for phrase in line.split("  ")]
        cleaned_text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limit response size for chat
        if len(cleaned_text) > 2000:
            cleaned_text = cleaned_text[:2000] + "... (content truncated for chat display)"
        
        return cleaned_text
    except Exception as e:
        return f"Error reading local content: {str(e)}"


def fetch_company_info(user_message: str = "") -> str:
    """
    Fetch company information from the most relevant URL based on user's query.
    """
    # Select the most relevant URL
    url_to_fetch = select_relevant_url(user_message) if user_message else COMPANY_URL
    
    # Check if we're in local testing mode
    if LOCAL_TESTING:
        return fetch_local_content(url_to_fetch)
    
    try:
        response = requests.get(url_to_fetch, timeout=10)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Extract text content and clean it up
        text_content = soup.get_text()
        
        # Clean up whitespace
        lines = [line.strip() for line in text_content.splitlines()]
        chunks = [phrase for line in lines for phrase in line.split("  ")]
        cleaned_text = ' '.join(chunk for chunk in chunks if chunk)
        
        # Limit response size for chat
        if len(cleaned_text) > 2000:
            cleaned_text = cleaned_text[:2000] + "... (content truncated for chat display)"
        
        return cleaned_text
    except Exception as e:
        # Minimal fallback if fetch fails
        return f"Unable to fetch company information at this time. Please try again later or contact support. (Error: {str(e)})"