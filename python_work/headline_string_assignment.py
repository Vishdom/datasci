#Write a function that takes a headline string and counts the number of words.
def count_words(headline):
    words = headline.split()
    return len(words)
# Example usage:
headline = "Breaking News: Major Event Unfolds"
word_count = count_words(headline)
print(f"The headline contains {word_count} words.")
# Output: The headline contains 5 words.
# The function splits the headline string into words using the split() method and returns the length of the resulting list, which represents the number of words in the headline.
# The function can be tested with different headline strings to verify its accuracy.
headline2 = "Statehood protest takes violent turn in Ladakh, BJP office set ablaze in Leh, Sonam Wangchuk claims 3-5 young people killed"
word_count2 = count_words(headline2)
print(f"The headline contains {word_count2} words.")

