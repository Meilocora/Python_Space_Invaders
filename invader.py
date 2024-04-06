from turtle import Turtle
from game_master import GameMaster

class Invader(Turtle, GameMaster):

    def __init__(self, game_color, x_pos, y_pos, id):
        super().__init__()
        self.penup()
        self.register_invader(game_color)
        self.shape("invader")
        self.setposition(x_pos, y_pos)
        self.setheading(90)
        self.speed = 20
        self.id = id

    def move(self, direction):
        new_x = self.xcor() + self.speed * direction
        self.goto(new_x, self.ycor())

    def destroy(self):
        self.hideturtle()
        self.clear()


