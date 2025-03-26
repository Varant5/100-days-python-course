from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
ball_speed = screen.numinput("Game difficulty", "Standard: 0.05 | Hard: 0.02", 0.1, minval=0.02, maxval=0.1)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball(ball_speed)
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while True:
    ball.move()
    time.sleep(ball.movement_speed)
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_ball(ball_speed)
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_ball(ball_speed)
        scoreboard.r_point()

    screen.update()

screen.exitonclick()