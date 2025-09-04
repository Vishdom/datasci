#Exercise on if using lists
usernames = ['admin', 'vish', 'suhas', 'varun', 'shantanu']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

#Exercise on if using lists
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
#Exercise on if using lists
current_users = ['vish', 'suhas', 'varun', 'shantanu', 'admin']
new_users = ['Vish', 'Suhas', 'Varun', 'Shantanu', 'Aniket']
current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that username is already taken. Please enter a new username.")
    else:
        print(f"Congratulations {new_user}, that username is available.")
#Exercise using ordinal number indicators
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
#This is the end of the program
