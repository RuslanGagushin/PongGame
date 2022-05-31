from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Make a program screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create a paddles
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
# Create a ball
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# move right puddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# move left puddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game is start
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Bounce from the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Get paddle touch
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) > -50 and ball.xcor() < -320:
        ball.bounce_x()

    # Make a scores
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
