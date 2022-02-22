from turtle import Turtle, Screen, textinput
import random


def check_win(racer: Turtle):
    if racer.xcor() > width / 2 - 50:
        return racer.color()[0]
    else:
        return "None"


screen = Screen()
width = 500
height = 500
screen.bgcolor("black")
screen.setup(width=width, height=height)

userinput = textinput(title="Who gon win", prompt="Pick a turtle").capitalize()

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
    subject.goto(x=-width / 2 + 10, y=y_placement)

win_status = "None"

while win_status == "None":
    for turtle in turtles:
        if win_status == "None":
            turtle.forward(random.randint(1, 100))
            win_status = check_win(turtle).capitalize()

if userinput == win_status: print(f"Your {userinput} turtle has won.")
else: print(f"Your {userinput.lower()} turtle has lost. {win_status} was the winner.")

screen.exitonclick()
