#This program will understand slices and lists
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
print(players[0:3])
#This will print the first three players in the list
print("Here are the middle three players on my team:")
print(players[1:4])
#If yyou omit the first index in a slice, Python automatically starts your slice at the beginning of the list
print(players[:4])
#This will print the first four players in the list
#If you omit the second index in a slice, Python automatically goes to the end of the list
print(players[2:])
#This will print the players from index 2 to the end of the list
#If you use a negative index, Python will count back from the end of the list
print("Here are the last three players on my team:")
print(players[-3:])
#This will print the last three players in the list
#If you use a negative second index
print(players[-4:-1])
#This will print the players from index -4 to -1 (not including -1)
#You can also use slices to create a new list
my_favorite_players = players[:]
print("My favorite players are:")
print(my_favorite_players)
#This will print all the players in the list


