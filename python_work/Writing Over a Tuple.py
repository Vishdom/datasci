#You can't modify a tuple, but you can redefine it entirely. This means you can assign a new tuple to the same variable name.
dimensions = (200, 50)
print("Original dimensions:")
for dimensions in dimensions:
    print(dimensions)

# Redefining the entire tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimensions in dimensions:
    print(dimensions)
# Attempting to modify an individual element will result in an error
# dimensions[0] = 300  # This will raise a TypeError
# print(dimensions[0])
# The above line is commented out to prevent the error from stopping the program.
# This will give an error because tuples are immutable and cannot be changed
# Note: Tuples are defined by the presence of a comma; parentheses are optional but they look neater and more readable

