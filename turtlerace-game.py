from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make Your Bet!", prompt="Which turtle will win the race? Enter a color: ")
color = ['red', "orange", "yellow", "green", "blue", 'purple']
y_position = [-80, -50, -20, 10, 40, 70]

all_turtle = []
for index in range (6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_position[index])
    all_turtle.append(new_turtle)

if user_input in color:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've win! The {winning_color} turtle is the winner")
                break
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
                break
        
        random_forward = random.randint(0,10)
        turtle.fd(random_forward)

screen.exitonclick()