import turtle


class Alien(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("#c6fa1b")
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=1)
        # self.setheading(90)
        self.showturtle()
        self.speed(1)

    def remove(self):
        self.hideturtle()  # Hide the turtle
        self.clear()

    def move_right(self):
        self.setx(self.xcor() + 0.4)

    def move_left(self):
        self.setx(self.xcor() - 0.4)
