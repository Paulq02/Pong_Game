from turtle import Turtle




class Paddle(Turtle):
    """
    Creates the two paddles at the start of the game, takes a position argument when object is created which tells where the paddle is 
    displayed on the screen
    """
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.shape("square")
        self.color("white")
        self.speed(10)
        self.goto(position)
        
        
        
        
    def left_paddle_up(self):
        """
        Method is used to move the left paddle upwards
        """
        self.forward(20)


    def left_paddle_down(self):
        """
        Method is used to move the left paddle downwards
        """
        self.backward(20)


    def right_paddle_up(self):
        """
        Method is used to move the right paddle upwards
        """
        self.forward(20)

    def right_paddle_down(self):
        """
        Method is used to move the right paddle downwards
        """
        self.backward(20)


    









