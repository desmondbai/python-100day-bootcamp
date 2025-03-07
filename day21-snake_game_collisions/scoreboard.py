from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.setpos(0,350)
        
    
    def display_score(self):
        self.clear()
        self.write(f"Total Score:{self.score}",align="center",font=('Arial',24,"normal"))
        
        
    def game_over(self):
        self.home()
        self.write("Game Over",align="center",font=('Arial',24,"normal"))

    
