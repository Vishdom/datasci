#This program is to test numerical values using python
age = 19
age == 19
print(age == 19)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
#The expression answer != 42 evaluates to True because the value of answer is not equal to 42.

if age < 21:
    print("You are not old enough to legally drink in the US.")
age = 34
age > 65
print(age < 65)
#Using and to check multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
print(age_0 >= 21 and age_1 >= 21)
age_1 = 23
age_0 >= 21 and age_1 >= 21
print(age_0 >= 21 and age_1 >= 21)

#Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
mushrooms = 'mushrooms' in requested_toppings
print('mushrooms' in requested_toppings)
'pepperoni' in requested_toppings
print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")



