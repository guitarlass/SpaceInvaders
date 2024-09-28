import turtle


class Ship(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("triangle")
        self.color("dark blue")
        self.penup()
        self.goto(0, -280)
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(90)
        self.showturtle()


    def move_right(self):
        if self.xcor() < 380:
            new_x = self.xcor() + 10
            self.setx(new_x)

    def move_left(self):
        if self.xcor() > -380:
            new_x = self.xcor() - 10
            self.setx(new_x)
