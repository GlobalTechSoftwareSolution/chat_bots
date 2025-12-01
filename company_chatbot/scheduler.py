"""
Scheduler module for company chatbot.
This module handles scheduled updates of information from URLs.
"""

import asyncio
import logging
from datetime import datetime, time
import threading
import time as time_module
from company_logic import crawl_relevant_pages, BASE_URL
from microbots import MICROBOTS

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def update_microbot_information():
    """
    Update microbot information by crawling relevant pages.
    """
    try:
        logger.info(f"Starting scheduled update at {datetime.now()}")
        
        # Crawl the website to discover relevant pages
        crawled_urls = crawl_relevant_pages(BASE_URL)
        
        # Clear the existing cache to force refresh
        from company_logic import CRAWLED_URLS
        CRAWLED_URLS.clear()
        
        # Update with new crawled URLs
        CRAWLED_URLS.update(crawled_urls)
        
        logger.info(f"Successfully updated URLs: {list(CRAWLED_URLS.keys())}")
        return True
    except Exception as e:
        logger.error(f"Error during scheduled update: {str(e)}")
        return False

def run_scheduler():
    """
    Run the scheduler to update information daily at midnight.
    """
    while True:
        # Get current time
        now = datetime.now()
        
        # Calculate time until next midnight
        tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0)
        if tomorrow <= now:
            tomorrow = tomorrow.replace(day=tomorrow.day + 1)
        
        # Calculate seconds until midnight
        seconds_until_midnight = (tomorrow - now).total_seconds()
        
        logger.info(f"Next update scheduled for {tomorrow}")
        logger.info(f"Sleeping for {seconds_until_midnight} seconds")
        
        # Sleep until midnight
        time_module.sleep(seconds_until_midnight)
        
        # Perform the update
        update_microbot_information()
        
        # Small delay to ensure we don't run multiple times in the same second
        time_module.sleep(1)

def start_scheduler_in_background():
    """
    Start the scheduler in a background thread.
    """
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    logger.info("Scheduler started in background thread")
    return scheduler_thread

# Start the scheduler when this module is imported
if __name__ != "__main__":
    start_scheduler_in_background()