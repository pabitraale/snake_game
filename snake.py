from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20

class Snake:
    def __int__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for pos in POSITION:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(pos)
            self.snakes.append(new_snake)



