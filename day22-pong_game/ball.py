from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.speed("fastest")
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
    
    def move(self,step=10,trace_time=.01):
        x, y = self.pos()
        self.goto(x + (step*self.x_direction), y + (step*self.y_direction))
        time.sleep(trace_time)


