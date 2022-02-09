from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_pos = -90
is_race_on = False

for new_color in colors:
    turtle_color = new_color
    new_color = Turtle(shape="turtle")
    new_color.color(turtle_color)
    new_color.penup()
    new_color.goto(x=-230, y=y_pos)
    turtles.append(new_color)
    y_pos += 33

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() < 220:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)
        else:
            winner = turtle.pencolor()
            is_race_on = False
            continue

if winner == user_bet:
    print(f"{winner} won and you placed your bet correctly!")
else:
    print(f"{winner} won and you placed your bet incorrectly!")

screen.exitonclick()