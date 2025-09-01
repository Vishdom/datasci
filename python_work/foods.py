#This program helps in udnerstanding on how to copy a list
foods = ['pizza', 'burger', 'pasta', 'salad', 'sushi']
friends_foods = foods [:]
print("My favorite foods are:")
print(foods)

print("n/My friend's favorite foods are:")
print(friends_foods)
#This will print all the foods in the list
#Adding new food items to each list
#To prove that we actually have two separate lists, let's add a new food to each list
foods.append('ice cream')
foods.append('tacos')
friends_foods.append('ramen')
friends_foods.append('steak')
print("My favorite foods are now:")
print(foods)

print("n/My friend's favorite foods are now:")
print(friends_foods)
