import turtle
from ship import Ship
screen = turtle.Screen()

screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
ship = Ship()

screen.listen()
screen.onkeypress(ship.move_right, "Right")
screen.onkeypress(ship.move_left, "Left")

screen.exitonclick()
