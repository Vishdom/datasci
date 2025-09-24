import os

# --- Robust path setup ---
script_dir = os.path.dirname(os.path.abspath(__file__))  # folder of this script
file_path = os.path.join(script_dir, "headlines.txt")    # full path to the file

# --- Read the file ---
with open(file_path, "r") as file:
    headlines = [h.strip() for h in file.readlines()]

# --- Sort headlines by length (descending) ---
headlines_sorted = sorted(headlines, key=len, reverse=True)

# --- Get top 3 longest headlines ---
top_n = 3
top_headlines = headlines_sorted[:top_n]

# --- Print results with word counts ---
print(f"Top {top_n} longest headlines:\n")
for i, headline in enumerate(top_headlines, 1):
    word_count = len(headline.split())
    print(f"{i}. {headline} ({word_count} words)")
