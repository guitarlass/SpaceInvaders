import turtle
from ship import Ship
from alien import Alien
from bullet import Bullet
from letter_brick import LetterBrick
from textboard import TextBoard
from endtext_lable import EndTextLabel
import random
import time

screen = turtle.Screen()

screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.tracer(0)

score = 0
lives = 3
bullets = []
aliens = []
obstacles = []
alien_bullets = []

ship = Ship()
scoreboard = TextBoard((-390, 275), "Score", score)
lifesboard = TextBoard((326, 275), "Lives", lives)

alien_x_pos = -200
alien_y_pos = 150
while alien_x_pos <= 200 and alien_y_pos <= 200:
    new_alien = Alien(alien_x_pos, alien_y_pos)
    aliens.append(new_alien)
    alien_x_pos += 40
    if alien_x_pos > 200:
        alien_y_pos += 50
        alien_x_pos = -200

# draw obstacle words
letters = [
    # V
    [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ],

    # I
    [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1]
    ],

    # S
    [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ],

    # S (Same as above)
    [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ],

    # D
    [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0]
    ],

    # E
    [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],

    # V (Same as the first "V")
    [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0]
    ]
]
start_x = -370
space = 0
for letter in letters:
    y = 0
    for pos_list in letter:
        x = start_x
        for item in pos_list:
            if item == 1:
                letter_brick = LetterBrick(x, y, "grey")
                obstacles.append(letter_brick)
            x += 20
        y -= 20
    start_x += 100 + 10

cool_down_time = 1
last_shot_time = 0


def create_ship_bullet():
    global last_shot_time
    current_time = time.time()

    if current_time-last_shot_time >= cool_down_time:
        new_bullet = Bullet((ship.xcor(), ship.ycor()), "dark green")
        bullets.append(new_bullet)
        last_shot_time = current_time


def create_alien_bullet():
    if aliens:  # Check if there are any aliens
        alien_ = random.choice(aliens)
        new_alien_bullet = Bullet((alien_.xcor(), alien_.ycor()), "#c6fa1b")
        alien_bullets.append(new_alien_bullet)
        # Schedule the next bullet creation
    screen.ontimer(create_alien_bullet, 300)


def setup_ship_controls(ship_instance):
    screen.onkeypress(ship_instance.move_right, "Right")
    screen.onkeypress(ship_instance.move_left, "Left")


screen.listen()
setup_ship_controls(ship)
screen.onkey(create_ship_bullet, "space")

moving_right = True


def move_aliens_right():
    reached_boundary = False
    for alien_ in aliens:
        alien_.move_right()
        if alien_.xcor() >= 380:  # If any alien reaches the right boundary
            reached_boundary = True
    if reached_boundary:
        return True
    return False


def move_aliens_left():
    reached_boundary = False
    for alien_ in aliens:
        alien_.move_left()
        if alien_.xcor() <= -390:  # If any alien reaches the left boundary
            reached_boundary = True
    if reached_boundary:
        return True
    return False


# Start the first bullet creation
create_alien_bullet()

game_on = True

while game_on:
    screen.update()
    if moving_right:
        if move_aliens_right():  # If right boundary is reached, change direction
            moving_right = False
    else:
        if move_aliens_left():  # If left boundary is reached, change direction
            moving_right = True

    for bullet in bullets:
        # screen.ontimer(bullet.move, 1000)
        bullet.move()
        for alien in aliens:
            if alien.distance(bullet.xcor(), bullet.ycor()) < 20:  # Adjust collision range
                bullet.remove()
                bullets.remove(bullet)
                alien.remove()
                aliens.remove(alien)
                score += 10
                scoreboard.update_board("Score", score)
        for obstacle in obstacles:
            if obstacle.distance(bullet.xcor(), bullet.ycor()) < 20:  # Adjust collision range
                bullet.remove()
                bullets.remove(bullet)
                obstacle.remove()
                obstacles.remove(obstacle)
                score += 5
                scoreboard.update_board("Score", score)
        for alien_bullet in alien_bullets:
            if alien_bullet.distance(bullet.xcor(), bullet.ycor()) < 10:
                bullet.remove()
                bullets.remove(bullet)
                alien_bullet.remove()
                alien_bullets.remove(alien_bullet)
                score += 10
                scoreboard.update_board("Score", score)
        if bullet.is_off_screen():
            bullet.remove()
            bullets.remove(bullet)

    for alien_bullet in alien_bullets:
        alien_bullet.move_alien_bullet()
        for obstacle in obstacles:
            if obstacle.distance(alien_bullet.xcor(), alien_bullet.ycor()) < 20:  # Adjust collision range
                alien_bullet.remove()
                alien_bullets.remove(alien_bullet)
                obstacle.remove()
                obstacles.remove(obstacle)
        # hits ship
        if ship.distance(alien_bullet.xcor(), alien_bullet.ycor()) < 20:  # Adjust collision range
            ship.hideturtle()
            ship.clear()
            print("lost")
            alien_bullet.remove()
            alien_bullets.remove(alien_bullet)
            if lives > 0:
                print("create ship")
                ship = Ship()
                setup_ship_controls(ship)
            lives -= 1
            lifesboard.update_board("Lives", lives)
        if alien_bullet.is_off_screen():
            alien_bullet.remove()
            alien_bullets.remove(alien_bullet)
        if lives == 0:
            game_on = False
            end_text = EndTextLabel("Game Over!")
            end_text.update_text_with_bg(f"Game Over!\nYour Score is {score}", "black")
        if not aliens:
            game_on = False
            end_text = EndTextLabel("You Won!")
            end_text.update_text_with_bg(f"You Won!\nYour Score is {score}", "black")

screen.mainloop()
