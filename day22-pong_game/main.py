from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball


WIDTH = 800
HEIGHT = 600
COLLISION_BUFFER = 10
# Set up new screen
screen = Screen()

screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
screen.title("pong")



screen.tracer(0)
# Create paddles
paddles = []
paddle_right = Paddle((350,0),len=5)
paddles.append(paddle_right)

paddle_left = Paddle((-350,0),len=5)
paddles.append(paddle_left)


# Spawn a ball
ball = Ball()


screen.listen()

screen.onkeypress(paddle_right.move_up,"Up")
screen.onkeypress(paddle_right.move_down,"Down")

screen.onkeypress(paddle_left.move_up,"w")
screen.onkeypress(paddle_left.move_down,"s")



is_on = True
while is_on:
    screen.update()
    ball.move(trace_time=.01,step=2)
    
    
    # 1. Bouncing off of ceiling and floor
    if abs(ball.pos()[1]) > (HEIGHT / 2) - 50:
        # Change the sign of direction multiplier
        ball.y_direction *= -1

    # 2. Bouncing off of paddles
    print([paddle.segments for paddle in paddles])

    # 2.1 Calculate minimal distance between ball and all of the paddles
    min_dist_ball_segment = min([ball.distance(segment) for paddle in paddles for segment in paddle.segments])

    # 2.2 Change direction when minimal distance is smaller than collision_buffer
    if min_dist_ball_segment <= COLLISION_BUFFER:
        ball.x_direction *= -1

    
    


screen.exitonclick()