from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        """
        keeps score of the Left and Right paddles, inherits from the Turtle module
        creates two attributes l_points and r_points which will keep track of each paddles score"""
        super().__init__()
        
        self.l_points = 0
        self.r_points = 0
        self.r_starting_score()
        self.l_starting_score()
        


    def r_wins(self):
        """
        This method is called if this paddle wins the game. Writes across the middle of the screen letting the user know they've won
        """
        self.goto(0, 0)
        self.hideturtle()
        self.color("white")
        self.write("Right Player Wins!", align="center", font=("Courier", 20, "normal"))

    def l_wins(self):
        """
        This method is called if this paddle wins the game. Writes across the middle of the screen letting the user know they've won
        """
        self.goto(0, 0)
        self.hideturtle()
        self.color("white")
        self.write("Left Player Wins!", align="center", font=("Courier", 20, "normal"))


    def l_score(self):
        """
        Keeps an updated score during the game. After a point is scored the screen is cleared removing the previous score 
        adding 1 to the paddles score then the method controlling the writing/displaying of the score is called,  allowing the new updated score
        to be displayed in it's place
        """
        self.clear()
        self.l_points += 1
        self.l_starting_score()
        self.r_starting_score()

    def r_score(self):
        """
        Keeps an updated score during the game. After a point is scored the screen is cleared removing the previous score 
        adding 1 to the paddles score then the method controlling the writing/displaying of the score is called,  allowing the new updated score
        to be displayed in it's place
        """
        self.clear()
        self.r_points += 1
        self.r_starting_score()
        self.l_starting_score()
        


    

    def l_starting_score(self):
        """
        This method is called when a Scoreboard object is created, it displays the starting score 0 - 0 represeting the left and right paddles starting score.
        the self.l_points is the attribute of the left paddle which holds a value of 0 to begin with and is increased by 1 if the paddle hits the ball
        """
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-350, 260)
        self.write(f"Left player score:{self.l_points}", align="left", font=("Courier", 20, "normal") )

    def r_starting_score(self):
        """
        This method is called when a Scoreboard object is created, it displays the starting score 0 - 0 represeting the left and right paddles starting score.
        the self.r_points is the attribute of the right paddle which holds a value of 0 to begin with and is increased by 1 if the paddle hits the ball
        """
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(350, 260)
        self.write(f"Right player score:{self.r_points}", align="right",font=("Courier", 20, "normal") )


    

            

        

        
        



    