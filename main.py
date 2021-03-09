from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        print("bounce")
        ball.bounce_x()

    if ball.xcor() > 400 or ball.xcor() < -400:
        ball = Ball()

    ball.move()
screen.exitonclick()
