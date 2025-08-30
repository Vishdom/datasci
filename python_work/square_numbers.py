#This is an example of listing square numbers using a for loop and range()
squares = []
for valuue in range(1, 15):
    square = valuue ** 2
    squares.append(square)
    print(squares)

#to wrie this code in a more concise way, we can use the following code
squares = []
for value in range(1, 15):
    squares.append(value ** 2)
print(squares)

#to write this code in an even more concise way, we can use list comprehension
squares = [value ** 2 for value in range(1, 15)]
print(squares)

