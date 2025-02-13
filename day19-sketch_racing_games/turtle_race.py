# 1. Prompt window asking user to bet on a turtle
# 2. Turtles lined up bottom up, moving from left to right.
# 3. Random step-size assigned to each turtle at each step
# 4. First one reaching the right-edge is the winner



#Turtle functions:
    #Turtle.teleport: move without drawing
    #Turtle.forward: move forward



from turtle import Screen,Turtle,colormode
from numpy import linspace
from random import randint

colormode(255)
NUM_TURTLES = 10
STEPS = 200









screen = Screen()

width,height = screen.screensize()


# Asking user for number of turtles
num_turtles = int(screen.numinput(title="Turtle Race", prompt="How many turtles you want to put in the race?"))



# Draw the finishing line
line_drawer = Turtle(visible=False)
line_drawer.teleport(width/2,height/2)
line_drawer.setheading(-90)
line_drawer.forward(height)




print(num_turtles)
# Calculate y coordinates of the turtles
y_coords = linspace(-height/2,height/2,num_turtles+2)[1:-1]


# Initialize, name and line up all the turtles
turtles = {}
print("Ok now, let's name all of your turtles")
for i in range(num_turtles):
    name = screen.textinput(title="Turtle Race", prompt=f"Give a name to turtle number {i+1}")
    turtle_temp = Turtle(visible=False,shape="turtle")
    turtles[name] = turtle_temp

    # Assign a random color
    r,g,b = (randint(0,255) for _ in range(3))
    turtle_temp.color(r,g,b)
    
    # Line up the turtle
    turtle_temp.teleport(-width/2,y_coords[i])
    turtle_temp.showturtle()
    turtle_temp.penup()
    

    











def move_turtles():
    for t in turtles.values():
        t.forward(randint(1, 5))  # Move randomly
    screen.update()


def check_winners(x_finish):
    max_x = width/2
    for name,turtle in turtles.items():
        #find the turtle with max x_coord, return it if it's pass the finishing line
        x_turtle = turtle.pos()[0]
        if x_turtle > max_x:
            max_x = x_turtle
            winner = name
    
    if max_x > x_finish:
        return winner

        


for _ in range(STEPS):
    move_turtles()

    winner = check_winners(width/2)

    if winner:
        print(f"The winner is {winner}!")

        # Setting colors of lost turtles to black
        [turtles[t].color("black") for t in turtles.keys() if t != winner]
        break
        



screen.exitonclick()





