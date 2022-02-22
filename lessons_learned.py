# creating objects in for loop
from turtle import Turtle

all_turtles = []

# creating 100 turtles
for i in range(0, 100):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
