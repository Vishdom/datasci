# Journalist's Source List Manager

# Step 1: Create a list of sources
sources = ["Reuters", "AP", "BBC", "NDTV"]

print("Current sources:", sources)

# Step 2: Add a new source
sources.append("The Hindu")
print("\nAdded The Hindu:", sources)

# Step 3: Remove a source you don’t use anymore
sources.remove("NDTV")
print("\nRemoved NDTV:", sources)

# Step 4: Sort sources alphabetically (temporary)
print("\nSorted temporarily:", sorted(sources))

# Step 5: Sort permanently
sources.sort()
print("\nSorted permanently:", sources)

# Step 6: Find how many sources you have
print("\nTotal sources:", len(sources))

# Step 7: Try to access a source safely
index_to_check = 3
if index_to_check < len(sources):
    print("\nSource at index 3:", sources[index_to_check])
else:
    print("\nThat source index doesn’t exist!")
#Step 8: Adding 2-3 more sources and print the final list
sources.append("Al Jazeera")
sources.append("CNN")
sources.append("The Guardian")
print("\nFinal sources list:", sources)
#Step 9: Remove oneusing del instead of remove()
del sources[-1]
print("\nRemoved last source using del:", sources)
#Step 10: Pretend you’re monitoring breaking news outlets only → make a new smaller list from the main one.
breaking_news = sources[:3]
print("\nBreaking news outlets:", breaking_news)
#Step 11: Print the smaller list
print("\nFinal smaller list of breaking news outlets:", breaking_news)
#Step 12: Print the original list to show it’s unchanged
print("\nOriginal sources list remains unchanged:", sources)
#Step 13: Reverse the order of the original list and print it
sources.reverse()

