from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 20:
        food.random_food_location()
        snake.extend_snake()
        score.increase_score()

    # Detect collision with wall
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280
            or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -300):
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.snakes[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
