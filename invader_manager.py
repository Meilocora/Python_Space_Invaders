from invader import Invader
from boss_invader import BossInvader
from game_master import GameMaster
import numpy as np
import random


class InvaderManager():
    def __init__(self, game_color):
        self.all_invaders = []
        self.game_color = game_color
        self.create_invaders()
        self.moving_direction = -1
        self.moves = 0
        self.moving_counter = 0

    def create_invaders(self):
        invader_id = 0
        for x_coord in range(-200, 200, 40):
            for y_coord in range(200, 400, 50):
                new_invader = Invader(self.game_color, x_coord, y_coord, invader_id)
                invader_id += 1
                self.all_invaders.append(new_invader)

    def handle_invaders(self, game_master, game_speed, boss_invader = None):
        self.moving_counter += 1
        if self.moving_counter >= game_speed:
            self.moving_counter = 0
            self.move_invaders()
            self.shoot(game_master, game_speed)
        if boss_invader and boss_invader.health > 0:
            self.handle_boss_invader(game_master, boss_invader)

    def move_invaders(self):
        if not -6 <= self.moves <= 6:
            self.moving_direction *= -1
        self.moves += self.moving_direction
        for invader in self.all_invaders:
            invader.move(self.moving_direction)

    def shoot(self, game_master, game_speed):
        for invader in self.all_invaders:
            random_shot = random.randint(-3*game_speed, 3*game_speed)
            if random_shot == 0:
                game_master.add_projectile(invader.xcor(), invader.ycor(), -1, min([1/game_speed*5, 2]), self.game_color)

    def handle_boss_invader(self, game_master, boss_invader):
        boss_invader.move()
        random_shot = random.randint(0, 3)
        if random_shot == 0:
            game_master.add_projectile(boss_invader.xcor(), boss_invader.ycor(), -1, 1.5, self.game_color)

    def delete_invader(self, invader):
        self.all_invaders = [valid_invader for valid_invader in self.all_invaders if valid_invader.id != invader.id]
        invader.destroy()