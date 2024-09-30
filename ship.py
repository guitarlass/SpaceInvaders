import turtle
from bullet import Bullet


class Ship(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("triangle")
        self.color("dark green")
        self.penup()
        self.goto(0, -305)
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(90)
        self.showturtle()
        self.position_ship()

    def position_ship(self):
        self.goto(0, -280)

    def move_right(self):
        if self.xcor() < 380:
            new_x = self.xcor() + 10
            self.setx(new_x)

    def move_left(self):
        if self.xcor() > -390:
            new_x = self.xcor() - 10
            self.setx(new_x)

    # def shoot(self, bullets):
    #     bullet = Bullet((self.xcor(), self.ycor()))
    #     bullets.append(bullet)
    #     bullet.shoot()
        # return bullet
