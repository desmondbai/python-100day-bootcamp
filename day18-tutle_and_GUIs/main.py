from turtle import Turtle,Screen,colormode,clearscreen
from random import randint,choice,random
from utils import *


#Initialize a turtle object with color and shape
my_turtle = Turtle()
my_turtle.shape("circle")
my_turtle.color("Red")





screen = Screen()




# Challenge1: Drawing a square
turtle_write_text(my_turtle,"Challenge1: Drawing a Square")
for _ in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)

clearscreen()




# Challenge2: Drawing a dashed line
turtle_write_text(my_turtle,"Challenge2: Drawing a dashed line")
for step in range(50):
    if step % 2 == 0:
        my_turtle.penup()
    else:
        my_turtle.pendown()

    my_turtle.forward(10)

clearscreen()





# Challenge3: Drawing Polygons
turtle_write_text(my_turtle,"Challenge3: Drawing Polygons",(-100,50))

for side in range(4,11):
    draw_polygon(my_turtle,side)

clearscreen()






# Challenge4: Random Walk

turtle_write_text(my_turtle,"Challenge4: Random Walk")

turtle_random_walk(my_turtle,speed=5,thickness=5,step_size=50,n_steps=50)

clearscreen()

        
        




# Challenge5: Drawing a Spirograph
my_turtle.shape("arrow")
my_turtle.width(1)

turtle_write_text(my_turtle,"Challenge5: Draw a Spiralgraph",(0,200))

        
draw_spiralgraph(my_turtle)




screen.exitonclick()






