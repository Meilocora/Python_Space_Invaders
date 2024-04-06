from turtle import Turtle
from game_master import GameMaster
import random
import time

LAST_SHOT = time.time()

class Defender(Turtle, GameMaster):

    def __init__(self, game_color):
        super().__init__()
        self.penup()
        self.speed = 20
        self.spawn(game_color)
        self.lifes = 2
        self.game_color = game_color

    def spawn(self, game_color):
        self.register_defender(game_color)
        self.shape("defender")
        self.setposition(0, -400)
        self.setheading(90)

    def go_right(self):
        if self.xcor() <= 310:
            new_x = self.xcor() + self.speed*(random.randint(90, 100)/100)  # add randomness to guarantee the defender can destroy all obstacles
            self.goto(x=new_x, y=self.ycor())

    def go_left(self):
        if self.xcor() >= -310:
            new_x = self.xcor() - self.speed*(random.randint(90, 100)/100) # add randomness to guarantee the defender can destroy all obstacles
            self.goto(x=new_x, y=self.ycor())

    def respawn(self):
        self.lifes -= 1
        if self.lifes == 1:
            self.setposition(-260, -400)
        elif self.lifes == 0:
            self.setposition(-320, -400)

    def shoot(self, game_master):
        global LAST_SHOT
        if (time.time() - LAST_SHOT) > 0.75:
            LAST_SHOT = time.time()
            game_master.add_projectile(self.xcor(), self.ycor(), 1, 1, self.game_color)