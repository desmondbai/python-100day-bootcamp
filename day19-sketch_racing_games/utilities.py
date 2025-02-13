from turtle import Turtle,Screen,colormode
from random import randint
from numpy import linspace






class Race:
    # Initialization of the racing game
    def __init__(self,GAME_NAME, STEPS,WIDTH,HEIGHT):
        self.screen = Screen()
        self.screen.setup(width=WIDTH,height=HEIGHT)
        self.steps = STEPS
        self.width = WIDTH
        self.height = HEIGHT
        self.num_turtles = int(self.screen.numinput(GAME_NAME,prompt="How many turtles do you want to put in the game?"))
        self.turtles = {}

                

        # Naming, Coloring and Lining up all of the turtles

        # Calculate the y coordinates of all of the turtles
        y_coords = linspace(-self.height/2,self.height/2,self.num_turtles+2)[1:-1]
        for i in range(self.num_turtles):
            name = self.screen.textinput(title=GAME_NAME, prompt=f"Give a name to turtle number {i+1}")
            turtle = Turtle(visible=False,shape="turtle")
            self.turtles[name] = turtle

            # Assign a random color
            colormode(255)
            r,g,b = (randint(0,255) for _ in range(3))
            turtle.color(r,g,b)
            
            # Line up the turtle
            turtle.teleport(-self.width/2,y_coords[i])
            turtle.showturtle()
            turtle.penup()

        # Step2: Draw a finishing line
        self.draw_finish()



    def draw_finish(self):
        line_drawer = Turtle(visible=False)
        line_drawer.teleport(self.width/2,self.height/2)
        line_drawer.setheading(-90)
        line_drawer.forward(self.height)

    
    def move_turtles(self):
        for t in self.turtles.values():
            t.forward(randint(1, 5))  # Move randomly
        self.screen.update()


    def check_winners(self):
        max_x = self.width/2
        for name,turtle in self.turtles.items():
            #find the turtle with max x_coord, return it if it's passed the finishing line
            x_turtle = turtle.pos()[0]
            if x_turtle > max_x:
                max_x = x_turtle
                winner = name
        
        if max_x > self.width/2:
            return winner
        
    def forward(self):
        for _ in range(self.steps):
            self.move_turtles()

            winner = self.check_winners()

            if winner:
                print(f"The winner is {winner}!")

                # Redening the winning turtle
                self.turtles[winner].color("red")

                # Blackening all the losing turtles
                [self.turtles[t].color("black") for t in self.turtles.keys() if t != winner]
                break
        
        self.screen.exitonclick()



if __name__ == "__main__":
    turtle_race = Race("Turtle Race",WIDTH=200,HEIGHT=200,STEPS=400)
    turtle_race.forward()
