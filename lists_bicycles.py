#this program is to learn on different kinds of lists in python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#To access an element in the list, write the name of the list followed by the ind
#ex of the item enclosed in square brackets
print(bicycles[0])
#To format the output, you can use the title() method to capitalize the first letter of each word in a string
print(bicycles[0].title())
#Index positions start at 0, so the second item has an index of 1. The second item of the list has an index of 1.
print(bicycles[1].title())
#Special syntax: If we ask for the item at index -1, pythoon always returns the last item in the list. This convention extends to other negative index too.
print(bicycles[-1].title())
print(bicycles[-2])
#Using individual values from the list
message = f"my first bicycle was a {bicycles[0].title()}."
print(message)

#Modifying lists- the syntax for modifying an element is similar to the syntaxfor accessing an element in the list.
motorcycles = ['honda', 'ducati', 'hyundai', 'suzuki']
motorcycles [0] = 'ducati'
print (motorcycles)
motorcycles.append('honda')
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[-3]
print(motorcycles)
motorcycles.insert(0, 'Royal Enfield')
print(motorcycles)
popped_motorcycle =motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles.append('ducati')
motorcycles.append('honda')
motorcycles.append('hyundai')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

