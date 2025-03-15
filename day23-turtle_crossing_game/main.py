from turtle import Turtle, Screen
import random
import time
from car import Car



random.seed(1234)

# Initial set-ups
WIDTH, HEIGHT = 600, 600
screen = Screen()
screen.bgcolor("white")
screen.setup(WIDTH,HEIGHT)
screen.tracer(0)
is_on = True






# Hyper-parameters
n_intervals = 5
frame = 0
cars = []
max_cars = 5



# Spawn the turtle racer
crossing_turtle = Turtle(shape="turtle")
crossing_turtle.penup()
crossing_turtle.speed(0)
crossing_turtle.seth(90)
crossing_turtle.goto(0,-HEIGHT//2 + 30)



while is_on:
    screen.update()
    if frame % n_intervals == 0:
        # Spawn random number of cars
        n_cars = random.randint(0,max_cars)
        for _ in range(n_cars):
            print(n_cars)
            car = Car(WIDTH/2,random.sample(range(-HEIGHT//2 + 100,HEIGHT//2+1),1)[0])
            cars.append(car)

    for car in cars:
        car.move()
        
    time.sleep(.5)
    frame += 1
    

    

screen.exitonclick()




