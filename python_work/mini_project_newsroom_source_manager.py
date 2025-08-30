# Interactive Newsroom Sources Manager with Categories

# Step 1: Start with a base list of sources
sources = {
    "Domestic": ["NDTV", "The Hindu"],
    "International": ["Reuters", "BBC", "AP"],
    "Tech": ["TechCrunch", "Wired"],
    "Finance": ["Bloomberg", "Financial Times"],
    "Sports": ["ESPN", "Sky Sports"],
    "Entertainment": ["Hollywood Reporter", "Variety"],
    "Health": ["Healthline", "WebMD"]
}

print("\n--- Welcome to Newsroom Sources Manager ---")

# Step 2: Show current categories
print("\nCurrent Categories and Sources:")
for category, srcs in sources.items():
    print(f"{category}: {srcs}")

# Step 3: Add new sources interactively with category
while True:
    new_source = input("\nEnter a new source to add (or type 'done' to finish): ")
    if new_source.lower() == "done":
        break

    category = input("Enter category (Domestic/International/Tech/Finance): ")
    if category not in sources:
        print("⚠️ Category not found. Adding it as a new one.")
        sources[category] = []

    sources[category].append(new_source)
    print(f"✅ Added {new_source} to {category}")

# Step 4: Remove a source interactively
remove_source = input("\nEnter a source to remove (or press Enter to skip): ")
if remove_source:
    found = False
    for category, srcs in sources.items():
        if remove_source in srcs:
            srcs.remove(remove_source)
            print(f"{remove_source} removed from {category}.")
            found = True
    if not found:
        print(f"{remove_source} not found in sources.")

# Step 5: Mark trusted sources
trusted_sources = []
print("\nMark trusted sources (type 'done' when finished):")
while True:
    trusted = input("Enter trusted source: ")
    if trusted.lower() == "done":
        break

    if any(trusted in srcs for srcs in sources.values()):
        trusted_sources.append(trusted)
        print(f"⭐ {trusted} marked as trusted.")
    else:
        print("⚠️ That source is not in your list.")

# Step 6: Show summary
print("\n--- Newsroom Summary ---")
for category, srcs in sources.items():
    print(f"{category} Sources: {sorted(srcs)}")

print("\nTrusted Sources:", trusted_sources)
print("Total Sources:", sum(len(srcs) for srcs in sources.values()))
print("Breaking News Outlets (top 3):", trusted_sources[:3])
print("\n--- End of Newsroom Sources Manager ---")

