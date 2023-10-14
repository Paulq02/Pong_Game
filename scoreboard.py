from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_points = 0
        self.r_points = 0
        self.r_starting_score()
        self.l_starting_score()


    def r_wins(self):
        self.goto(0, 0)
        self.hideturtle()
        self.color("white")
        self.write("Right Player Wins!", align="center", font=("Courier", 20, "normal"))

    def l_wins(self):
        self.goto(0, 0)
        self.hideturtle()
        self.color("white")
        self.write("Left Player Wins!", align="center", font=("Courier", 20, "normal"))


    def l_score(self):
        self.clear()
        self.l_points += 1
        self.l_starting_score()
        self.r_starting_score()

    def r_score(self):
        self.clear()
        self.r_points += 1
        self.r_starting_score()
        self.l_starting_score()
        


    

    def l_starting_score(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-350, 260)
        self.write(f"Left player score:{self.l_points}", align="left", font=("Courier", 20, "normal") )

    def r_starting_score(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(350, 260)
        self.write(f"Right player score:{self.r_points}", align="right",font=("Courier", 20, "normal") )
        
        



    