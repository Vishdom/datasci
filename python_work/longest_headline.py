# Open the file in read mode
with open("headlines.txt", "r") as file:
    headlines = file.readlines()

# Remove newline characters and extra spaces
headlines = [h.strip() for h in headlines]

# Find the longest headline
longest_headline = max(headlines, key=len)

print("The longest headline is:")
print(longest_headline)
