# 🧾 Pastebin Keyword Crawler

A Python tool that scrapes [Pastebin's public archive](https://pastebin.com/archive) for pastes containing

**crypto-related keywords** (like `bitcoin`, `crypto`, `wallet`, `BTC`, etc.) or **Telegram links**. It uses regular expressions to search the content of each paste and stores all matches in a structured `.jsonl` (JSON Lines) file.

---

## 🚀 Features

✅ Scrapes Pastebin’s archive to extract the latest **30 paste IDs**  
✅ Fetches content and scans for **keywords**  
✅ Identifies **crypto terms** and **Telegram (`t.me`) links**  
✅ Stores results in clean **JSONL format**  
✅ Logs activity to both **console** and `crawler.log`  
✅ Implements **rate limiting** to avoid getting blocked  

---

## 🛠 Setup Instructions

### ✅ Prerequisites

- Python 3.10
- Install required packages:
  ```bash
  pip install requests beautifulsoup4
  
**📦 Installation**
git clone https://github.com/your-username/pastebin-keyword-crawler.git
cd pastebin-keyword-crawler

**⚙️ Usage**
python pastebin_crawler.py
What it does:

## Scrapes latest 30 Pastebin paste links.

## Scans each paste for predefined keywords.

**Logs results in:**

keyword_matches.jsonl (JSONL format)

crawler.log (human-readable log

**🧾 Output Format**

{
  "source": "pastebin",
  "context": "Found crypto-related content in Pastebin paste ID abc123",
  "paste_id": "abc123",
  "url": "https://pastebin.com/raw/abc123",
  "discovered_at": "2025-05-16T10:00:00Z",
  "keywords_found": ["crypto", "bitcoin"],
  "status": "pending"
}

**📂 Sample Output (JSONL)**
{"source": "pastebin", "context": "Found crypto-related content in Pastebin paste ID xYzAbC", "paste_id": "xYzAbC", "url": "https://pastebin.com/raw/xYzAbC", "discovered_at": "2025-05-16T15:32:18Z", "keywords_found": ["bitcoin", "eth"], "status": "pending"}
{"source": "pastebin", "context": "Found Telegram links in Pastebin paste ID Abc123", "paste_id": "Abc123", "url": "https://pastebin.com/raw/Abc123", "discovered_at": "2025-05-16T15:32:24Z", "keywords_found": ["t.me"], "status": "pending"}
{"source": "pastebin", "context": "Found crypto-related content and Telegram links in Pastebin paste ID dEf456", "paste_id": "dEf456", "url": "https://pastebin.com/raw/dEf456", "discovered_at": "2025-05-16T15:32:30Z", "keywords_found": ["crypto", "t.me"], "status": "pending"}
**🖼️ Demonstration**

(![ExpectedOutput](https://github.com/user-attachments/assets/18b39ab4-fa46-4344-92b0-4aaed6d20e14)



