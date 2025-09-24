import requests
from bs4 import BeautifulSoup

url = "https://www.reuters.com/news/world"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching Reuters: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Extract all <h3> tags
headline_tags = soup.find_all("h3")
headlines = [tag.get_text().strip() for tag in headline_tags if len(tag.get_text().strip()) > 5]

if not headlines:
    print("No valid headlines extracted.")
    exit()

# Sort by length and pick top 5
headlines_sorted = sorted(headlines, key=len, reverse=True)
top_headlines = headlines_sorted[:5]

print("Top 5 longest Reuters headlines:\n")
for i, headline in enumerate(top_headlines, 1):
    print(f"{i}. {headline} ({len(headline.split())} words)")
