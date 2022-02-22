from turtle import Turtle, Screen

screen = Screen()
width = 500
height = 500
screen.bgcolor("black")
screen.setup(width=width, height=height)


red = Turtle(shape="turtle")
orange = Turtle(shape="turtle")
yellow = Turtle(shape="turtle")
green = Turtle(shape="turtle")
blue = Turtle(shape="turtle")
white = Turtle(shape="turtle")

red.color('red')
orange.color('orange')
yellow.color('yellow')
green.color('green')
blue.color('blue')
white.color('white')

turtles = [red, orange, yellow, green, blue, white]
for i in range(len(turtles)):
    subject = turtles[i]
    subject.penup()
    y_placement = -height / 6 * i + (height - 20) / 2
    subject.goto(x=-width/2+10, y=y_placement)





