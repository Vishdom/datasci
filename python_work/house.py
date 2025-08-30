name = input("What's your name? ")
if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
        print("Gryffindor")
elif name == "Draco":
        print("Slytherin")
elif name == "Pansy":
        print("Slytherin")
elif name == "Cedric":
        print("Hufflepuff")
elif name == "Hannah":
        print("Hufflepuff")
elif name == "Luna":
        print("Ravenclaw")
elif name == "Cho":
        print("Ravenclaw")
else:
        print("Who?")

#using logical operators
if name in ["Harry", "Hermione", "Ron"]:
    print("Gryffindor")
elif name in ["Draco", "Pansy"]:
    print("Slytherin")
elif name in ["Cedric", "Hannah"]:
    print("Hufflepuff")
elif name in ["Luna", "Cho"]:
    print("Ravenclaw")
else:
    print("Who?")


