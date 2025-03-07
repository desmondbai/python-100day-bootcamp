from turtle import Turtle,color


class Snake:
    def __init__(self,n_segments=5):
        self.segments = []
        self.create_snake(n_segments)
        self.head = self.segments[-1]
        self.tail = self.segments[0]


    def create_snake(self,n_segments):
        x_coord = 0
        for _ in range(n_segments):
            self.add_segment(x_coord,0)
            x_coord += 20 # Each square takes up 20 pixels in width

    def add_segment(self,x,y,ind=-1):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setpos(x,y)
        self.segments.insert(ind,segment)
    

    def extend_snake(self):
        #extending snake at its tail
        
        self.add_segment(self.tail.xcor(),self.tail.ycor(),0)
        
    def move(self):
        head = self.segments[-1]
        # Iterating thru all segments except for the 1st one whose movement is defined at a later stage
        for i,segment in enumerate(self.segments[:-1]):
            # Each segment (from the last one to the very first) is gonna follow through the position of its previous one
            segment.setpos(self.segments[i+1].pos())
        head.forward(20)    

    
    def head_east(self):
        if not self.head.heading() == 180:
            self.head.seth(0)

    def head_west(self):
        if not self.head.heading() == 0:
            self.head.seth(180)

    def head_north(self):
        if not self.head.heading() == 270:
            self.head.seth(90)

    def head_south(self):
        if not self.head.heading() == 90:
            self.head.seth(270)

        

        