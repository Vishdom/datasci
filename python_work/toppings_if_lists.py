#this program illustrates the use of if in lists
requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']
for for_topping in requested_toppings:
	print(f"Adding {for_topping}.")
print("\nFinished making your pizza!")

#What if the pizzeria runs out of green peppers?
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for for_topping in requested_toppings:
  if for_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now.")
  else:
    print(f"Adding {for_topping}.")
print("\nFinished making your pizza!")

#Checking that a list is not empty
requested_toppings = []
if requested_toppings:
  for for_topping in requested_toppings:
    print(f"Adding {for_topping}.")
  print("\nFinished making your pizza!")
else:
  print("Are you sure you want a plain pizza?")
#Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for for_topping in requested_toppings:
  if for_topping in available_toppings:
    print(f"Adding {for_topping}.")
  else:
    print(f"Sorry, we don't have {for_topping}.")
print("\nFinished making your pizza!")
#This is the end of the program


