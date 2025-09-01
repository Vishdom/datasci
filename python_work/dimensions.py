#Tuples
#A Tuple looks like a list, but it is immutable (cannot be changed).
#In a Tuple, you use parentheses instead of square brackets.
#Once a tuple is defined, you can access its individual elements by using eacch item's index, just as in a list
dimensions = (200, 50)
print("Original dimensions:")
print(dimensions[0])
print(dimensions[1])
#Let's say that we need to change the dimensions of the object. You cannot change a tuple, but you can redefine the entire tuple
dimensions = (400, 100)
print("Modified dimensions:")
print(dimensions[0])
print(dimensions[1])
#Let's say that we need to change the dimensions of the object. You cannot change a tuple, but you can redefine the entire tuple
dimensions = (400, 100)
print("Modified dimensions:")
dimensions[0] = 300
print(dimensions[0])
print(dimensions[1])
#This will give an error because tuples are immutable and cannot be changed

#NOTE:Tuples are defined by the presence of a comma; parentheses are optional but they look neater and more readable
#For example, the following is also a valid tuple
my_tuple = 3,
print(type(my_tuple))


