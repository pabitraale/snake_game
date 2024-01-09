from turtle import Turtle, Screen

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Score")

#created 3 turtle that create rectangle snake shape
x_cor = 0
for _ in range(3):
    t = Turtle()
    t.penup()
    current_position = t.xcor() + x_cor
    print(current_position)
    t.setposition(current_position, 0)
    t.shape("square")
    t.color("white")
    x_cor += -20





screen.exitonclick()