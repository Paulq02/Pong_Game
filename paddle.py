from turtle import Turtle




class Paddle(Turtle):

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
        self.forward(20)


    def left_paddle_down(self):
        self.backward(20)


    def right_paddle_up(self):
        self.forward(20)

    def right_paddle_down(self):
        self.backward(20)


    









