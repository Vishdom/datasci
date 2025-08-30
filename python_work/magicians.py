#this is an example of loooping through an entire list
magicians =["alice","david","carolina"]
for magician in magicians:
	print(magician)

#following program will help in orinting a message to each magician
for magician in magicians:
  print(f"{magician.title()}, that was a great trick!")
  print(f"I can't wait to see your next trick, {magician.title()}.\n")

#doing something after the loop is done
print("Thank you, everyone. That was a great magic show!")
#Avoiding indentation errors
#the following code will give an indentation error
magicians =["alice","david","carolina"]
for magician in magicians:
  print(magician)
#print(f"{magician.title()}, that was a great trick!")
  print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
#the last print statement should not be indented, otherwise it will be part of the for loop and will be executed for each magician in the list
#the correct code is as follows
magicians =["alice","david","carolina"]
for magician in magicians:
  print(magician)
  print(f"{magician.title()}, that was a great trick!")
  print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
