from turtle import Turtle, Screen, mode


mode("standard")
screen = Screen()
tim = Turtle()


def rotate_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)



def rotate_counterclockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)



def move_forward():
    tim.forward(10)
    


def move_backward():
    tim.backward(10)


def clear():
    screen.resetscreen()
    tim.penup()
    tim.home()
    tim.pendown()




screen.listen()

screen.onkeypress(move_forward,"w")
screen.onkeypress(move_backward,"s")
screen.onkeypress(rotate_counterclockwise,"d")
screen.onkeypress(rotate_clockwise,"a")
screen.onkeypress(clear,"h")

screen.exitonclick()

