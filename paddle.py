from turtle import Turtle




class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_1()
        self.paddle_2()
        
        


    def paddle_1(self):
        self.paddle1 = Turtle()
        self.paddle1.penup()
        self.paddle1.setheading(90)
        self.paddle1.shapesize(stretch_len=5)
        self.paddle1.shape("square")
        self.paddle1.color("white")
        self.paddle1.goto((-350, 0))

    def paddle_2(self):
        self.paddle2 = Turtle()
        self.paddle2.penup()
        self.paddle2.setheading(90)
        self.paddle2.shapesize(stretch_len=5)
        self.paddle2.shape("square")
        self.paddle2.color("white")
        self.paddle2.goto((350, 0))


       
        

    
        


    

    def move_up(self):
        self.paddle2.forward(20)

    def move_down(self):
        self.paddle2.backward(20)





