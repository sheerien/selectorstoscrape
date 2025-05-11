import re
from typing import List, Optional
from fake_useragent import UserAgent
import httpx
import re

def fetch_html(url: str, referer:str="") -> str:
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Referer": referer
    }

    try:
        with httpx.Client(headers=headers, timeout=10.0, follow_redirects=True) as client:
            response = client.get(url)
            response.raise_for_status()
            return response.text

    except httpx.HTTPStatusError as e:
        print(f"❌ HTTP error while fetching {url}: {e.response.status_code} - {e}")
    except httpx.RequestError as e:
        print(f"❌ Network error while fetching {url}: {e}")
    except Exception as e:
        print(f"🚨 Unexpected error while fetching {url}: {e}")
    
    return ""