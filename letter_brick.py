import turtle

class LetterBrick(turtle.Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.shapesize(stretch_wid=1, stretch_len=1)
        # self.setheading(90)
        self.showturtle()

    def remove(self):
        self.hideturtle()  # Hide the turtle
        self.clear()


