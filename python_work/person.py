#Using dictionaries to store information about a person
person = {
	"first_name": "John",
	"last_name": "Doe",
	"age": 30,
	"city": "New York"
}
print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])
print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}.")
#Use a dictionary to store people's favorite numbers
favorite_numbers = {
  "Alice": 7,
  "Bob": 42,
  "Charlie": 3.14,
  "Diana": 100
}
print(f"Alice's favorite number is {favorite_numbers['Alice']}.")
print(f"Bob's favorite number is {favorite_numbers['Bob']}.")
print(f"Charlie's favorite number is {favorite_numbers['Charlie']}.")
print(f"Diana's favorite number is {favorite_numbers['Diana']}.")
#Make a dictionary of glossary terms
glossary = {
  "variable": "A named location used to store data in memory.",
  "function": "A block of code that performs a specific task.",
  "loop": "A sequence of instructions that repeats until a certain condition is met.",
  "dictionary": "A collection of key-value pairs used to store related data."
}
print(f"Variable: {glossary['variable']}")
print(f"Function: {glossary['function']}")
print(f"Loop: {glossary['loop']}")
print(f"Dictionary: {glossary['dictionary']}")
#Add more terms to the glossary
glossary["list"] = "An ordered collection of items that can be changed."
glossary["tuple"] = "An ordered collection of items that cannot be changed."
glossary["set"] = "An unordered collection of unique items."
print(f"List: {glossary['list']}")
print(f"Tuple: {glossary['tuple']}")
print(f"Set: {glossary['set']}")
#Loop through the glossary and print each term and its definition
for term, definition in glossary.items():
    print(f"{term.capitalize()}: {definition}")
#Make a dictionary of rivers and the countries they flow through
rivers = {
  "Nile": "Egypt",
  "Amazon": "Brazil",
  "Yangtze": "China",
  "Mississippi": "USA"
}
for river, country in rivers.items():
    print(f"The {river} flows through {country}.")
#Loop through the dictionary keys
for river in rivers.keys():
    print(river)
#Loop through the dictionary values
for country in rivers.values():
    print(country)
#Use a set to remove duplicate values when looping through dictionary values
for country in set(rivers.values()):
    print(country)
#Make a dictionary of people and their favorite languages
favorite_languages = {
  "Alice": "Python",
  "Bob": "JavaScript",
  "Charlie": "C++",
  "Diana": "Java"
}
#List of people to check
people = ["Alice", "Bob", "Eve", "Frank"]
for person in people:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person}.")
    else:
        print(f"{person}, please take our poll!")

