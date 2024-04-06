import random
from turtle import Turtle
from game_master import GameMaster
from explosion import Explosion


class ScreenManager(Turtle, GameMaster):

    def __init__(self, game_color):
        super().__init__()
        self.penup()
        self.pencolor(game_color)
        self.hideturtle()
        self.lifes = []
        self.set_lifebar(game_color)
        self.score = 0
        self.draw_score()
        self.game_color = game_color
        self.all_explosions = []

    def draw_bottom_line(self):
        self.setposition(-340, -430)
        self.pendown()
        self.goto(340, -430)
        self.penup()

    def draw_logo(self):
        self.setposition(10, -485)
        self.write("SPACE INVADERS", align="center", font=("Segoe", 32, "bold"))

    def set_lifebar(self, game_color):
        self.register_defender(game_color)
        self.create_defender(-320, -465)
        self.create_defender(-260, -465)

    def create_defender(self, x_coord, y_coord):
        new_def = Turtle()
        new_def.shape("defender")
        new_def.setposition(x_coord, y_coord)
        new_def.setheading(90)
        self.lifes.append(new_def)

    def draw_score(self):
        self.clear()
        self.draw_bottom_line()
        self.draw_logo()
        self.setposition(280, -465)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 15, "normal"))

    def increase_score(self, points):
        self.score += points
        self.draw_score()

    def loose_life(self):
        self.lifes[-1].hideturtle()
        self.lifes[-1].clear()
        self.lifes.pop()

    def set_explosion(self, type, x_coord, y_coord):
        random_id = random.randint(0, 1000000)
        new_explosion = Explosion(type, x_coord, y_coord, self.game_color, random_id)
        self.all_explosions.append(new_explosion)

    def calc_explosions(self):
        for explosion in self.all_explosions:
            explosion.decrease_timer()
            if explosion.timer <= 0:
                self.all_explosions = [valid_explosion for valid_explosion in self.all_explosions if valid_explosion.id != explosion.id]
                explosion.destroy()

    def game_over(self, status, remaining_invaders, boss_health = 4, turns = 1):
        self.draw_score()
        message = (f"You {status}!\n"
                   f"Killed Invaders: {40-remaining_invaders}/40\n"
                   f"Total points: {self.score}\n"
                   f"Time: {turns/10} seconds\n")
        if boss_health == 0:
            message += "Boss Invader - Killed!"
        self.setposition(-275, -350)
        self.write(f"{message}", align="left", font=("Courier", 24, "normal"))
