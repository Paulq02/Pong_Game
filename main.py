from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from net import Net



#Below is the basic screen setup
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Paul Pong Game")
screen.tracer(0)

#Here we have the left and right paddle objects taking input on where to be displayed on the screen when the game starts
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

#Ball object 
ball = Ball()

#Scoreboard Object
score = ScoreBoard()

#Net object
net = Net()




#Listen method is called to listen to specific buttons to be pressed to control the paddle movement
screen.listen()

#Up key controls the upward movement of the right paddle
screen.onkey(r_paddle.right_paddle_up, "Up")

#Down key controls the downward movement of the right paddle
screen.onkey(r_paddle.right_paddle_down, "Down")

# w key controls the upward movement of the left paddle
screen.onkey(l_paddle.left_paddle_up, "w")

# s key controls the downward movement of the left paddle
screen.onkey(l_paddle.left_paddle_down, "s")


game_on = True
while game_on:
    # I Used the sleep function to control the speed of the ball - whenever the ball hits a paddle the start_speed attribute is increased 
    time.sleep(ball.start_speed)
    #Screen is updated constantly
    screen.update()
    #The move_ball method keeps the ball in motion increasing by 10 on the X and Y axis
    ball.move_ball()
    
    


    #Screen is set to 600 height so if the ball hits 280 on the Y axis the Y movement attribute gets multiplied by -1 
    #Making it reverse course (downward)if it was heading up or (upward) if the ball was heading downward
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Here we check if the ball has went past 320 on the X axis and if the ball is within 50 pixels of the right paddle
    #If the ball makes contact with the right paddle the right paddle gets 1 point added
    #The ball speed is increased, plus the X movement attribute is multiplied by -1 making it reverse course
    if ball.xcor() > 320:
        if ball.distance(r_paddle) < 50:
            score.r_score()
            ball.bounce_x()
            

    #Here we check if the ball has went past -320 on the X axis and if the ball is within 50 pixels of the left paddle
    #If the ball makes contact with the left paddle the left paddle gets 1 point added
    #The ball speed is increased, plus the X movement attribute is multiplied by -1 making it reverse course
    if ball.xcor() < -320:
        if ball.distance(l_paddle) < 50:
            score.l_score()
            ball.bounce_x()
            
    #Here we check if the ball has went past 395 on the X axis, meaning the ball never made contact with a paddle.
    #The ball is reset to the middle of the screen and the ball is then served in the opposite direction it came from
    if ball.xcor() > 395:
        ball.reset_position()

    #Here we check if the ball has went past -395 on the X axis, meaning the ball never made contact with a paddle.
    #The ball is reset to the middle of the screen and the ball is then served in the opposite direction it came from
    if ball.xcor() < -395:
        ball.reset_position()

    #Here we check if either paddle has scored 5 points to win IF the other player has less than 5 points
    if score.l_points == 5 and score.r_points < score.l_points and ball.xcor() > 385:
        game_on = False
        score.l_wins()
    if score.r_points == 5 and score.l_points < score.r_points and ball.xcor() < -385:
        game_on = False
        score.r_wins()


        
        


        
        
       
        

        
        
        
        
    
        
        


       
        
        
        
        
    

    












screen.exitonclick()