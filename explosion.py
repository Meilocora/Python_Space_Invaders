from turtle import Turtle
from game_master import GameMaster

class Explosion(Turtle, GameMaster):

    def __init__(self, type, x_coord, y_coord, game_color, id):
        super().__init__()
        self.spawn(type, x_coord, y_coord, game_color)
        self.timer = 1
        self.id = id


    def spawn(self, type, x_coord, y_coord, game_color):
        if type == "small_explosion":
            self.register_small_explosion(game_color)
        else:
           self.register_explosion(game_color)
        self.shape(type)
        self.setposition(x_coord, y_coord)

    def decrease_timer(self):
        self.timer -= 0.1

    def destroy(self):
        self.hideturtle()
        self.clear()