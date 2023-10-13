from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0


    def game_over(self):
        self.hideturtle()
        self.color("white")
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))



    