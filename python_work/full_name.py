#This program is an example of f-strings in Python.
first_name ="ada"
last_name = "lovelace"
full_name =f"{first_name} {last_name}"
print(full_name)

#You can use f-strings to compose coomplete messages using information associated with a variable
first_name ="ada"
last_name = "lovelace"
full_name =f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#You can use f-strings to compose a message, and then assign the entire message to a variable
first_name ="ada"
last_name = "lovelace"
full_name =f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#Adding whitespaces to strings with tabs or new lines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Stripping whitespace from strings
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#Removing prefixes in a string
nostrach_url ='http://www.nostrach.com'
nostrach_url = nostrach_url.removeprefix('http://')
print(nostrach_url)

#Assigning a new variable to the string with the prefix removed
simple_url = nostrach_url.removeprefix('http://')
print(simple_url)

#Removing suffixes in a string
nostrach_url ='www.nostrach.com'
nostrach_url = nostrach_url.removesuffix('.com')
print(nostrach_url)

#Assigning a new variable to the string with the suffix removed
simple_url = nostrach_url.removesuffix('.com')
print(simple_url)

#You can use the methods lstrip(), rstrip(), and strip() to remove whitespace characters from the left side, right side, or both sides of a string.
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#You can use the methods removeprefix() and removesuffix() to remove specific prefixes or suffixes from a string.
nostrach_url ='http://www.nostrach.com'
nostrach_url = nostrach_url.removeprefix('http://')
print(nostrach_url)
simple_url = nostrach_url.removeprefix('http://')
print(simple_url)
nostrach_url ='www.nostrach.com'
nostrach_url = nostrach_url.removesuffix('.com')
print(nostrach_url)
simple_url = nostrach_url.removesuffix('.com')
print(simple_url)



