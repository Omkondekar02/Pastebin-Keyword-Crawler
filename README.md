# Pastebin-Keyword-Crawler
This is a simple Python tool that automatically scrapes Pastebin's public archive to find pastes containing crypto-related keywords (like bitcoin, crypto, wallet, BTC, etc.) or Telegram links. The tool uses regular expressions to scan the content of each paste and stores any matches in a structured .jsonl file (JSON Lines format).

**Features**
Scrapes Pastebin's archive to extract the latest 30 paste IDs
Fetches the content of each paste and checks for keywords
Identifies crypto-related terms and Telegram links
Stores matches in a structured JSONL format
Includes logging for tracking and validation
Implements rate limiting to avoid being blocked
