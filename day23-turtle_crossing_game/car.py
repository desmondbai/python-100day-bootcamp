from turtle import Turtle,colormode
from random import randint
colormode(255)

class Car(Turtle):
    def __init__(self,x,y):
        
        # Spawning a car object at the given location
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(x,y)
        self.shapesize(1,2.5)
        self.speed_value = 1
        self.speed(self.speed_value)
        r,g,b = (randint(0,255) for _ in range(3))
        self.color(r,g,b)
    
    def accelerate(self):
        # Increment the car's speed by 1 unit
        self.speed_value += 1
        self.speed(self.speed_value)

    
    def move(self):
        # Moving from left to right
        x,y = self.pos()
        self.goto(x - 20,y)
        
        

