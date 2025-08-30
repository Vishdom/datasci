#write a python program to count numbers to 20 using for loop to print the numbers from 1 to 20, inclusive
for number in range(1, 21):
    print(number)
#a python program to make a list of numbers from 1 to one million and then use a for loop to print the numbers.
#if the output is taking tooo long,stop it by pressing ctrl + c or by closing the output window
#numbers = list(range(1, 1000001))
#for number in numbers:
    #print(number)

#A python program to make a list of numbers from 1 to 1 million and then use min() and max() to print the smallest and largest number in the list
#also use sum() to print the sum of all the numbers in the list
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#A python program to use a for loop to print the first 20 odd numbers
for number in range(1, 41, 2):
    print(number)

#A Pythoon program to make a list of the multiples of 3, from 3 to 300 . Use a for loop to print the numbers in your list
for number in range(3, 301, 3):
    print(number)
#A python program to make a list of the first 10 cubes using a for loop
cubes = []
for number in range(1, 11):
    cubes.append(number ** 3)
print(cubes)
print("The first three cubes are:")
for cube in cubes[:3]:
    print(cube)
print("Three middle cubes are:")
for cube in cubes[3:7]:
    print(cube)

#Use a list comprehension to generate a list of the first 10 quadruple numbers
quadruples = [number ** 4 for number in range(1, 11)]
print(quadruples)
#Use a list comprehension to generate a list of the first 10 square roots
square_roots = [number ** 0.5 for number in range(1, 11)]
print(square_roots)
#write to program to use a list comprehension to generate a list of the first 10 square roots limiting to 2 decimal points
square_roots = [round(number ** 0.5, 2) for number in range(1, 11)]
print(square_roots)
#Write a program to use a list comprehension to generate a quadratic equation of the first 2 even numbers
quadratic_equation = [number ** 2 + 2 * number + 1 for number in range(2, 21, 2)]
print(quadratic_equation)
#write a program to generate a hyperbole of the first 10 numbers
hyperbole = [1 / number for number in range(1, 11)]
print(hyperbole)
#write a program to generate a list of the first 10 factorials using a for loop
factorials = []
factorial = 1
for number in range(1, 11):
    factorial *= number
    factorials.append(factorial)
print(factorials)
#write a program to generate the sum of the first 10 factorials using a for looop
sum_of_factorials = 0
for number in range(1, 11):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    sum_of_factorials += factorial
print(sum_of_factorials)
#write a program to generate a list of the first 10 prime numbers using a for loop
primes = []
for number in range(2, 30):
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    if len(primes) == 10:
        break
print(primes)

