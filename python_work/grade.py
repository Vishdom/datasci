#Using if, elif and else statements, write a program that asks the user to enter a score (0-100) and prints the corresponding grade based on the following criteria:
score =int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#using nested if
if score >= 0 and score <= 100:
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

#Using comparison range operators
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#Using ternary operator
print("Grade: A" if 90 <= score <= 100 else "Grade: B" if 80 <= score < 90 else "Grade: C" if 70 <= score < 80 else "Grade: D" if 60 <= score < 70 else "Grade: F")
