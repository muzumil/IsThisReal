import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return f"[ERROR] HTTP {response.status_code} while accessing {url}"

        soup = BeautifulSoup(response.text, "html.parser")

        # Try to grab the main article content
        paragraphs = soup.find_all('p')
        article_text = "\n\n".join([p.get_text() for p in paragraphs])

        if len(article_text.strip()) < 200:
            return "[ERROR] Article too short or poorly extracted."

        return article_text.strip()

    except Exception as e:
        return f"[ERROR extracting URL] {str(e)}"

