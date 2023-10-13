from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard




screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Paul Pong Game")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()




screen.listen()
screen.onkey(r_paddle.right_paddle_up, "Up")
screen.onkey(r_paddle.right_paddle_down, "Down")
screen.onkey(l_paddle.left_paddle_up, "w")
screen.onkey(l_paddle.left_paddle_down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()



    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.xcor() > 320:
        if ball.distance(r_paddle) < 50:
            ball.bounce_x()


    if ball.xcor() < -320:
        if ball.distance(l_paddle) < 50:
            ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()
        
        


        
        
       
        

        
        
        
        
    
        
        


       
        
        
        
        
    

    












screen.exitonclick()