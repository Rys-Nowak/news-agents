import requests
import json
import time
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, user_agent=None, sleep_between_requests=1):
        self.headers = {
            "User-Agent": user_agent or "Mozilla/5.0"
        }
        self.sleep = sleep_between_requests

    def fetch_article(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")
            title_tag = soup.find("h1")
            paragraphs = soup.find_all("p")

            title = title_tag.text.strip() if title_tag else "Brak tytułu"
            body = "\n".join(p.text.strip() for p in paragraphs if len(p.text.strip()) > 40)

            return {
                "url": url,
                "title": title,
                "content": body
            }
        except Exception as e:
            print(f"[ERROR] Problem fetching {url}: {e}")
            return None

    def scrape(self, urls):
        """Scrapes a list of URLs and returns a list of parsed articles."""
        articles = []
        for url in urls:
            print(f"[INFO] Fetching: {url}")
            article = self.fetch_article(url)
            if article:
                articles.append(article)
            time.sleep(self.sleep)
        return articles

    def scrape_and_save(self, urls, output_path="articles.json"):
        """Scrapes URLs and saves the results to a JSON file."""
        articles = self.scrape(urls)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        print(f"[INFO] Saved {len(articles)} articles to {output_path}")