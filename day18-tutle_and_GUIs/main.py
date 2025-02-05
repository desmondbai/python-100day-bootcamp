from turtle import Turtle, Screen, colormode, Screen,mode
import colorgram
import random



SPEED = 0
THICKNESS = 5
N_MAIN = 50 #VERTIAL
N_CROSS = 50 #HORIZONTAL
RADIUS = 5
colormode(255)
mode("standard")

if __name__ == "__main__":
    
    my_turtle = Turtle()
    my_turtle.shape("circle")

    #Pick color palette from downloaded image
    colors = colorgram.extract("img.jpeg",10)
    colors = [tuple(color.rgb) for color in colors]
    print(colors)

    # Start screen
    screen = Screen()
    screen.screensize(800,600)
    width,height = screen.screensize()
    print(width,height)



    # Initialize turtle position
    #my_turtle.hideturtle()
    my_turtle.shape("arrow")
    my_turtle.penup()
    my_turtle.setpos(-width/2,-height/2)
    my_turtle.setheading(0)


    



    # Calculate step size for x and y axis
    step_cross = width / N_CROSS
    step_main = height / N_MAIN


    print(screen.screensize())
    

    # Initialize properties with param set-ups
    my_turtle.width(THICKNESS)
    my_turtle.speed(SPEED)



    



    def draw_circle(turtle:Turtle,radius:int,color_palette:list):
        
        # Store original heading
        original_heading = turtle.heading()
        # Fix drawing direction to only clock-wise
        turtle.setheading(0)
        turtle.fillcolor(random.choice(color_palette))
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()

        # Reset to original heading after circle is drawn
        turtle.setheading(original_heading)




    for _ in range(N_MAIN):
        draw_circle(my_turtle,RADIUS,colors)
        for _ in range(N_CROSS - 1):
            my_turtle.forward(step_cross)
            draw_circle(my_turtle,RADIUS,colors)        

        opposite_heading = my_turtle.heading() + 180
        my_turtle.setheading(90)
        my_turtle.forward(step_main)
        my_turtle.setheading(opposite_heading)
        print(my_turtle.heading())

        

    screen.exitonclick()


