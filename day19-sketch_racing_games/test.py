from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)



# Listen on Keyboard Input
screen.listen()

# Define a function responding to specific keystroke
screen.onkey(key="space",fun=move_forwards) #Expecting a function (with no args) and a key



screen.exitonclick()

