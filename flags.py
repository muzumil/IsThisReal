import heapq
from collections import defaultdict
from urllib.parse import urlparse

class Flag:
    def __init__(self, message, severity):
        self.message = message
        self.severity = severity

    def __lt__(self, other):
        return self.severity > other.severity  # Max-heap behavior

def extract_red_flags(article_text):
    flags = []
    if "!!!" in article_text or "shocking" in article_text.lower():
        heapq.heappush(flags, Flag("Clickbait-like language", 3))
    if "source" not in article_text.lower():
        heapq.heappush(flags, Flag("No source mentioned", 2))
    if len(article_text.split()) < 100:
        heapq.heappush(flags, Flag("Article is too short", 1))
    
    return flags


def word_frequency(text):
    freq = defaultdict(int)
    for word in text.split():
        freq[word.lower()] += 1
    return freq

def check_domain_trust(url):
    trusted = {"bbc.com", "reuters.com", "npr.org"}
    domain = urlparse(url).netloc
    return domain in trusted
