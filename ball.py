import time
from turtle import Turtle



class Ball(Turtle):
    """
    Ball is created when object is made, along with 3 attributes - the balls start speed and the default starting pace of the balls movement 
    on the X and Y axis
    """

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.start_speed = 0.1
        self.x_move = 10
        self.y_move = 10
    
        
        
    def move_ball(self):
        """
        Method controls the movement of the ball, X and Y coodinates are grabbed - Pace of the ball fluctuates from +10 or -10 depending on circumstances
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    

    def bounce_y(self):
        """
        If ball hits the top or bottom of the screen the Y axis movement is flipped - Multiplying the y_move attribute by -1
         changing the balls movement in the opposite direction
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        If the ball hits either paddle the x_move attribute is multiplied by -1 - changing the balls movement in the opposite direction.
        Also after each paddle collision the start_speed attribute is multiplied by 0.9 increasing the speed of the ball.

        """
        self.x_move *= -1
        self.start_speed *= 0.9

    def reset_position(self):
        """
        Method controls the ball being repositioned after a paddle miss. The ball is then placed at the middle of the screen.
        The ball speed is reset back to it's default speed (0.1). Also the bounce_x method is called, which controls the initial serve to start the game
        """
        self.goto(0, 0)
        self.start_speed = 0.1
        self.bounce_x()

    


   
        


        



    
    
        

        

    



        
        

    
        
