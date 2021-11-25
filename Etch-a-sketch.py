from turtle import Turtle, Screen

lal = Turtle()
lal.shape("classic")


def move_forward():
    lal.forward(10)


def move_backward():
    lal.backward(10)


def move_right():
    lal.right(10)


def move_left():
    lal.left(10)


def clear():
    lal.clear()
    lal.penup()
    lal.home()
    lal.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear)


screen.exitonclick()