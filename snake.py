from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.snake_head = self.snakes[0]

    def create_snake(self):
        for pos in POSITION:
            self.add_snake(pos)

    def move(self):
        for num in range(len(self.snakes)-1, 0, -1):
            new_xcor = self.snakes[num - 1].xcor()
            new_ycor = self.snakes[num - 1].ycor()
            self.snakes[num].goto(new_xcor, new_ycor)

        self.snakes[0].forward(20)

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.speed(3)
        new_snake.goto(position)
        self.snakes.append(new_snake)

    # Add snake at the end of the snake length
    def extend_snake(self):
        self.add_snake(self.snakes[-1].position())

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)



