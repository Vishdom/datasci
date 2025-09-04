#Imagine in shooting game, there are different alien colors. Each has a specific point value. write a program that prints the point value of the alien color with only if statements.
alien_color = 'red'
if 'green' in alien_color:
    print("You just earned 5 points!")
if 'yellow' in alien_color:
    print("You just earned 10 points!")
if 'red' in alien_color:
    print("You just earned 15 points!")

#Now, write the same program, but this time using if-elif-else statements.
alien_color = 'orange'
if 'green' in alien_color:
    print("You just earned 5 points!")
elif 'yellow' in alien_color:
    print("You just earned 10 points!")
elif 'red' in alien_color:
    print("You just earned 15 points!")
else:
    print("No points earned.")




