from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) #tracer turned off but it must be turned on later in the code

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score() 

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        #it needs to bounce back
        ball.bounce_y()

        #detect collision with the paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

        #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
