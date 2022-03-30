from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def reset_round(dir):
    ball.reset_pos(dir)
    l_pad.reset()
    r_pad.reset()


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_pad = Paddle("left")
r_pad = Paddle("right")
ball = Ball()
board = Scoreboard()

screen.listen()
screen.onkey(l_pad.move_up, 'w')
screen.onkey(l_pad.move_down, 's')
screen.onkey(r_pad.move_up, 'Up')
screen.onkey(r_pad.move_down, 'Down')

game_running = True
while game_running:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_pad) < 50 and ball.xcor() > 320) or (ball.distance(l_pad) < 50 and ball.xcor() < -320):
        ball.paddle_hit()

    if ball.xcor() > 380:
        board.l_point()
        reset_round("right")
    elif ball.xcor() < -380:
        board.r_point()
        reset_round("left")

    screen.update()
    time.sleep(ball.move_speed)

screen.exitonclick()
