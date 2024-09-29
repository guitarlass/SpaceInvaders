import turtle


class Bullet(turtle.Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=.2, stretch_len=1)
        self.setheading(90)
        self.showturtle()
        self.speed(1)
        self.step = 3

    def remove(self):
        self.hideturtle()  # Hide the turtle
        self.clear()

    def is_off_screen(self):
        if self.ycor() > 300:
            return True
        return False

    def move(self):
        self.sety(self.ycor() + self.step)

    def move_alien_bullet(self):
        self.sety(self.ycor() - self.step)
