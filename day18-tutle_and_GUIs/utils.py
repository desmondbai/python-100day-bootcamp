from turtle import Turtle,Screen,colormode,clearscreen
from random import randint,choice,random


def assign_pencolor(turtle:Turtle):
    """
    Assign random color to an turtle object, under colormode(255)
    """
    colormode(255)
    r,g,b = (randint(0,255) for _ in range(3))

    turtle.pencolor(r,g,b)



def turtle_write_text(turtle:Turtle,text:str,coord=(0,50)):
    """
    Write text with the turtle pen, putting it back to origin once finished
    """
    turtle.penup()
    turtle.color("black")
    turtle.hideturtle()
    turtle.setpos(coord)
    turtle.write(text)
    turtle.home()
    turtle.pendown()
    turtle.showturtle()




def draw_polygon(turtle:Turtle, n_sides:int,len_sides = 50):
    """
    Drawing a polygon of `n_sides` sides on Canvas
    """
    assign_pencolor(turtle)
    for _ in range(n_sides):
        turtle.right(360/n_sides)
        turtle.forward(len_sides)



def turtle_random_walk(turtle:Turtle,speed = 10, thickness = 1,step_size = 10, n_steps = 1000):
    turtle.pensize(width=thickness)
    turtle.speed(speed)
    for _ in range(n_steps):
        assign_pencolor(turtle)
        turtle.seth(randint(1,4) * 90)
        turtle.forward(step_size)


def draw_spiralgraph(turtle:Turtle,speed=0,steps=100,radius=100):
    """
    Draw spiralgraph of using a turtle object,
    Which is a series of circle, each attained by rotating the previous one to a certain angle and assigned a random color
    """
    turtle.speed(speed)
    for _ in range(steps):
        assign_pencolor(turtle)
        turtle.setheading(turtle.heading() +  360/steps)
        turtle.circle(100)
