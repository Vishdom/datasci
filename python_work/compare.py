x = int(input("What's x? "))
y = int(input("what's y?"))
if x < y:
    print("x is less than y")
if x> y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

#using elif
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

#using else
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
#using nested if
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
    if x - y < 10:
        print("but not by much")
else:
    print("x is equal to y")

#using if-elif-else instead of match case
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

#using logical operators
if x < y and y < 10:
    print("x is less than y and y is less than 10")
if x < y or y < 10:
    print("x is less than y or y is less than 10")
if not x < y:
    print("x is not less than y")

#using ternary operator
print("x is less than y" if x < y else "x is greater than or equal to y")

