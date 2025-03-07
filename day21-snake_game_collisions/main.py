from turtle import Turtle, Screen
from random import randint
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

N_START = 5
N_FRUITS = 2
WIDTH = 800
HEIGHT = 800



# Set up the screen
screen = Screen()
screen.setup(WIDTH,HEIGHT) #window size of screen
screen.screensize(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.tracer(0) # Disable tracer



                 


# Initializing a new snake
snake = Snake(5)


# Spawn food
food = Food()


# Listening on keystroke
screen.listen()



# Listen on keystrokes
screen.onkey(fun=snake.head_east,key="d")
screen.onkey(fun=snake.head_west,key="a")
screen.onkey(fun=snake.head_north,key="w")
screen.onkey(fun=snake.head_south,key="s")




# Start the game
is_on = True
scoreboard = ScoreBoard()
while is_on:
    time.sleep(.1)
    snake.move()
    screen.update()
    scoreboard.display_score()
    # Detect collision between snake and foods
    if snake.head.distance(food) <= 20:
        # Move food to a different random location
        food.refresh()
        # Extend snake body
        snake.extend_snake()
        scoreboard.score += 1
    
    # Detect collision between snake and walls
    if (abs(snake.head.xcor()) > (WIDTH/2 - 50)) or (abs(snake.head.ycor()) > (HEIGHT/2 - 50)):
        scoreboard.game_over()
        is_on = False

    # Detect collision with itself
    if min(snake.head.distance(body) for body in snake.segments[0:-1]) <= 10:
       scoreboard.game_over()
       is_on = False


screen.exitonclick()





