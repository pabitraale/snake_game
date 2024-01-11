from turtle import Turtle, Screen
from snake import Snake
import time

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Score")
screen.tracer(0)

snake = Snake()


# snake move forward
game_start = True
while game_start:
    screen.update()
    time.sleep(0.2)

    snake.move()




screen.exitonclick()