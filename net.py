from turtle import Turtle

POSITIONS = [(0, 280), (0, 240),(0, 200),(0, 160), (0, 120), (0, 80), (0, 40), (0, 0), (0, -40), (0, -80), (0, -120), (0, -160), (0, -200), (0, -240), (0, -280)]

class Net(Turtle):

    def __init__(self):
        super().__init__()
        
        self.screen_net()




    def screen_net(self):
       for position in POSITIONS:
            net_slice = Turtle()
            net_slice.penup()
            net_slice.setheading(90)
            net_slice.shapesize(stretch_len=1, stretch_wid=0.2)
            net_slice.color("white")
            net_slice.shape("square")
            net_slice.goto(position)
            