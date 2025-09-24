import requests
from bs4 import BeautifulSoup

# Fetch BBC News homepage
url = "https://www.bbc.com/news"
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching BBC News: {e}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Extract all <h3> tags (headlines are often here)
headline_tags = soup.find_all("h3")

# Get text and filter out very short or empty ones
headlines = [tag.get_text().strip() for tag in headline_tags if len(tag.get_text().strip()) > 10]

if not headlines:
    print("No valid headlines extracted.")
    exit()

# Sort by length descending
headlines_sorted = sorted(headlines, key=len, reverse=True)

# Take top 3
top_n = 3
top_headlines = headlines_sorted[:top_n]

# Print top headlines with word counts
print(f"Top {top_n} longest BBC headlines:\n")
for i, headline in enumerate(top_headlines, 1):
    word_count = len(headline.split())
    print(f"{i}. {headline} ({word_count} words)")
