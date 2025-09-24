import os  # at the top

# --- Robust path setup ---
script_dir = os.path.dirname(os.path.abspath(__file__))  # folder of this script
file_path = os.path.join(script_dir, "headlines.txt")    # full path to the file

# --- Read the file ---
with open(file_path, "r") as file:
    headlines = file.readlines()

# Remove newline characters
headlines = [h.strip() for h in headlines]

# Find the longest headline
longest_headline = max(headlines, key=len)

print("The longest headline is:")
print(longest_headline)
