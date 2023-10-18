from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from net import Net




screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Paul Pong Game")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()
net = Net()





screen.listen()
screen.onkey(r_paddle.right_paddle_up, "Up")
screen.onkey(r_paddle.right_paddle_down, "Down")
screen.onkey(l_paddle.left_paddle_up, "w")
screen.onkey(l_paddle.left_paddle_down, "s")


game_on = True
while game_on:
    
    time.sleep(ball.start_speed)
    screen.update()
    ball.move_ball()
    #print(f"X cordinate: {ball.xcor()}... Y cordinate: {ball.ycor()}")
    



    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.xcor() > 320:
        if ball.distance(r_paddle) < 50:
            score.r_score()
            ball.bounce_x()
            print(ball.start_speed)


    if ball.xcor() < -320:
        if ball.distance(l_paddle) < 50:
            score.l_score()
            ball.bounce_x()
            #print(ball.start_speed)

    if ball.xcor() > 395:
        ball.reset_position()

    if ball.xcor() < -395:
        ball.reset_position()

    if score.l_points == 5 and score.r_points < score.l_points and ball.xcor() > 385:
        game_on = False
        score.l_wins()
    if score.r_points == 5 and score.l_points < score.r_points and ball.xcor() < -385:
        game_on = False
        score.r_wins()


        
        


        
        
       
        

        
        
        
        
    
        
        


       
        
        
        
        
    

    












screen.exitonclick()