#!/usr/bin/env python3
"""
Pastebin Keyword Crawler
------------------------
This script scrapes Pastebin's public archive for pastes containing crypto-related keywords
or Telegram links and stores the matching pastes in a JSONL file.
"""

import requests
from bs4 import BeautifulSoup
import re
import json
import time
from datetime import datetime
import logging
import random

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("crawler.log"),
        logging.StreamHandler()
    ]
)

class PastebinCrawler:
    """A crawler for Pastebin that searches for specific keywords."""
    
    def __init__(self):
        self.archive_url = "https://pastebin.com/archive"
        self.raw_paste_url = "https://pastebin.com/raw/{}"
        self.output_file = "keyword_matches.jsonl"
        
        # Keywords to search for
        self.crypto_keywords = [
            "crypto", "bitcoin", "ethereum", "blockchain", "btc", "eth",
            "altcoin", "defi", "nft", "token", "coin", "wallet", "mining"
        ]
        self.telegram_keywords = ["t.me"]
        
        # Headers to mimic a browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
    
    def get_archive_pastes(self):
        """Scrape the Pastebin archive to get the latest 30 paste IDs."""
        try:
            response = requests.get(self.archive_url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            paste_links = soup.select('table.maintable tr td:nth-child(1) a')
            
            paste_ids = []
            for link in paste_links:
                href = link.get('href')
                if href and href.startswith('/'):
                    paste_ids.append(href[1:])  # Remove the leading '/'
            
            logging.info(f"Found {len(paste_ids)} paste IDs from the archive")
            return paste_ids
        
        except requests.RequestException as e:
            logging.error(f"Error fetching archive: {e}")
            return []
    
    def get_paste_content(self, paste_id):
        """Fetch the content of a paste by its ID."""
        url = self.raw_paste_url.format(paste_id)
        try:
            # Add a small delay to avoid rate limiting
            time.sleep(random.uniform(1, 3))
            
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        
        except requests.RequestException as e:
            logging.error(f"Error fetching paste {paste_id}: {e}")
            return None
    
    def check_keywords(self, content):
        """Check if the content contains any of the keywords."""
        if not content:
            return []
        
        keywords_found = []
        
        # Check for crypto keywords
        for keyword in self.crypto_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', content.lower()):
                keywords_found.append(keyword)
        
        # Check for Telegram links
        for keyword in self.telegram_keywords:
            if keyword in content.lower():
                keywords_found.append(keyword)
        
        return keywords_found
    
    def save_match(self, paste_id, keywords_found):
        """Save the paste information to the output file."""
        url = self.raw_paste_url.format(paste_id)
        timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # Create context message based on keywords
        context_keywords = []
        if any(k for k in keywords_found if k in self.crypto_keywords):
            context_keywords.append("crypto-related content")
        if any(k for k in keywords_found if k in self.telegram_keywords):
            context_keywords.append("Telegram links")
        
        context = f"Found {' and '.join(context_keywords)} in Pastebin paste ID {paste_id}"
        
        match_data = {
            "source": "pastebin",
            "context": context,
            "paste_id": paste_id,
            "url": url,
            "discovered_at": timestamp,
            "keywords_found": keywords_found,
            "status": "pending"
        }
        
        with open(self.output_file, 'a') as f:
            f.write(json.dumps(match_data) + '\n')
        
        logging.info(f"Saved match for paste {paste_id} with keywords: {keywords_found}")
    
    def run(self):
        """Run the crawler to find and save matching pastes."""
        # Create/clear the output file
        with open(self.output_file, 'w'):
            pass
        
        paste_ids = self.get_archive_pastes()
        total_matches = 0
        
        for i, paste_id in enumerate(paste_ids):
            logging.info(f"Processing paste {i+1}/{len(paste_ids)}: {paste_id}")
            
            content = self.get_paste_content(paste_id)
            if content:
                keywords_found = self.check_keywords(content)
                if keywords_found:
                    self.save_match(paste_id, keywords_found)
                    total_matches += 1
                else:
                    logging.info(f"No keywords found in paste {paste_id}")
            
        logging.info(f"Crawler completed. Found {total_matches} matching pastes out of {len(paste_ids)}")

# Main execution block
if __name__ == "__main__":
    crawler = PastebinCrawler()
    crawler.run()