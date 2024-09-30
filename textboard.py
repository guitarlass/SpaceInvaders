import turtle


class TextBoard(turtle.Turtle):
    def __init__(self, position, text, value):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(position)
        # self.setheading(90)
        self.write(f"{text}: {value}", align="left", font=("Arial", 12, "bold"))

    def update_board(self, text, value):
        self.clear()
        self.write(f"{text}: {value}", align="left", font=("Arial", 12, "bold"))
