from turtle import Turtle
import random
# Behaviors:
    # Randomly spawn on the screen
    # Every time snake touches the food, move to a new random location
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest") #omit the process of spawning and moving to a position
        self.refresh()
        
    def refresh(self):
        self.goto((random.randint(-300,300) for _ in range(2)))


