#This is an example of a if looop statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#checking for Equality
car = 'bmw'
print(car == 'bmw')

#When the value of car is anything other than 'bmw', the expression car == 'bmw' evaluates to False.
car = 'audi'
print(car == 'bmw')

