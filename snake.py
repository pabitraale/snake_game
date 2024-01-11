from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for pos in POSITION:
            new_snake = Turtle("square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(pos)
            self.snakes.append(new_snake)

    def move(self):
        for num in range(len(self.snakes)-1, 0, -1):
            new_xcor = self.snakes[num - 1].xcor()
            new_ycor = self.snakes[num - 1].ycor()
            self.snakes[num].goto(new_xcor, new_ycor)

        self.snakes[0].forward(20)




