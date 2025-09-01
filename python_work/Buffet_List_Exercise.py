#A buffet style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple. Use a for loop to print each food the restaurant offers.
foods = ('pizza', 'burger', 'pasta', 'salad', 'sushi')
print("The buffet offers the following foods:")
for food in foods:
    print(food)
#Try to modify one of the items, and make sure that Python rejects the change.
#foods[0] = 'ice cream'  # This will raise a TypeError
#print(foods[0])
#The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foods = ('tacos', 'steak', 'pasta', 'salad', 'sushi')
print("\nThe updated buffet offers the following foods:")
for food in foods:
    print(food)

