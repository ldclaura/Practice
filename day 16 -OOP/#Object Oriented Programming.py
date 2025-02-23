#Object Oriented Programming

#procedural programming is messy

#has and does, attributes (variable) and methods (function)
#waiter (class)
#has: plate, tables responsible
#does: take order and take payment
#create multiple different waiters 

#car = CarBlueprint() - class CarBlueprint(), car is object
from turtle import Turtle, Screen
from prettytable import PrettyTable
import another_module

print(another_module.another_variable)

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)



my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


table = PrettyTable()
table.align = "l"
table.add_column("Pokemon", ["Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Water", "Fire", "Grass"])
print(table)
#car.speed (car object, speed attribute)
#car.stop() (car object, stop method)

#python packages
#pypi.org (python package index)
