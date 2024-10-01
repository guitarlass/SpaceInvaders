import turtle


class EndTextLabel(turtle.Turtle):
    def __init__(self, message):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_wid=10, stretch_len=4)
        self.penup()
        self.goto(0, 0)
        self.fillcolor("black")
        # self.setheading(90)
        # self.write(f"{message}", align="left", font=("Arial", 12, "bold"))
        self.speed(0)  # to speed up drawing

    # draw a rectangle background
    def draw_background(self, width, height, bg_color):
        self.fillcolor(bg_color)
        self.begin_fill()

        # Draw rectangle (assuming center alignment for text)
        for _ in range(2):
            self.forward(width / 2)
            self.right(90)
            self.forward(height)
            self.right(90)
            self.forward(width / 2)

        self.end_fill()

    # write text with a background
    def update_text_with_bg(self, new_text, bg_color):
        self.clear()  # Clear previous text and background
        self.goto(0, 85)  # Adjust position
        self.draw_background(400, 100, bg_color)

        # Write the text on top of the bg
        self.goto(0, 0)  # Move to position
        self.write(new_text, align="center", font=("Arial", 24, "normal"))
