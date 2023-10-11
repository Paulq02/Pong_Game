from turtle import Turtle, Screen
from paddle import Paddle
import time




screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Paul Pong Game")
screen.tracer(0)


paddle = Paddle()




screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")


game_on = True
while game_on:
    screen.update()











screen.exitonclick()