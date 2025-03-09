from turtle import Turtle

class Paddle():
    def __init__(self,position:tuple,len=5):
        super().__init__()
        self.segments = []
        x,y = position
        for _ in range(len):
            segment = self.create_segment(x,y)
            self.segments.append(segment)
            y-=20
    
    def create_segment(self,x,y):
        segment = Turtle()
        segment.shape("square")
        segment.shapesize(1,1,1)
        segment.color("white")
        segment.penup()
        segment.setpos(x,y)
        return segment


    def move_up(self):
        for segment in self.segments:
            x,y = segment.pos()
            segment.goto(x,y+20)

    def move_down(self):
        for segment in self.segments:
            x,y = segment.pos()
            segment.goto(x,y-20)

