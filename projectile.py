from turtle import Turtle
import random


class Projectile(Turtle):
    def __init__(self, x_coord, y_coord, direction, speed, game_color):
        super().__init__()
        self.id = random.randint(0, 1000000)
        self.shape("square")
        self.shapesize(stretch_len=0.15, stretch_wid=0.75)
        self.penup()
        self.color(game_color)
        self.setposition(x_coord, y_coord + 25 * direction)
        self.direction = direction
        self.speed = speed*10

    def move(self):
        new_y = self.ycor() + self.speed * self.direction
        self.goto(self.xcor(), new_y)

    def destroy(self):
        self.hideturtle()
        self.clear()