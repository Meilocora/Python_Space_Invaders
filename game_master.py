from turtle import Screen, Shape
from projectile import Projectile

DEFENDER_POLY = ((-20, 0), (-20, 12), (-4, 12), (-4, 20), (0, 26), (4, 20), (4, 12), (20, 12), (20, -8), (15, 0), (-15, 0), (-20, -8), (-20,0))

INVADER_POLY = ((-10,0), (-10, 10), (0, 20), (10, 10), (10, 0), (5, 0), (15, -15), (5, -5), (0, -10), (-5, -5), (-15, -15), (-5, 0), (-10, 0))

HEALTH_4 = ((-25, 0), (-25, 5), (25, 5), (25, 0))
HEALTH_3 = ((-25, 0), (-25, 5), (12.5, 5), (12.5, 0))
HEALTH_2 = ((-25, 0), (-25, 5), (0, 5), (0, 0))
HEALTH_1 = ((-25, 0), (-25, 5), (-12.5, 5), (-12.5, 0))

BOSS_INVADER_POLY = ((-25, 0), (-25, 5), (-15, 15), (-8, 15), (-8, 20), (-4, 23),
                     (4, 23), (8, 20), (8, 15), (15, 15), (25, 5), (25, 0), (32, -8), (25, -4), (-25, -4), (-32, -8), (-25, 0))

SMALL_EXPLOSION_POLY = ((0, 7), (1.5, 3), (5, 5), (3.5, 1.5), (7, 0),
                  (3, -1.5), (5, -5), (1.5, -3), (0, -7),
                  (-1.5, -3), (-5, -5), (-3.5, -1.5), (-7, 0),
                  (-3.5, 1.5), (-5, 5), (-1.5, 3), (0, 7))

EXPLOSION_POLY = ((0, 20), (5, 8), (15, 15), (10, 5), (20, 0),
                  (10, -5), (15, -15), (5, -8), (0, -20),
                  (-5, -8), (-15, -15), (-10, -5), (-20, 0),
                  (-10, 5), (-15, 15), (-5, 8), (0, 20))

class GameMaster():
    def __init__(self):
        self.all_projectiles = []
        self.screen = Screen()
        self.turns = 0

    def register_defender(self, game_color):
        defender = Shape("compound")
        defender.addcomponent(DEFENDER_POLY, game_color)
        self.screen.register_shape("defender", defender)

    def register_invader(self, game_color):
        invader = Shape("compound")
        invader.addcomponent(INVADER_POLY, game_color)
        self.screen.register_shape("invader", invader)

    def register_boss_invader(self, game_color):
        boss_invader = Shape("compound")
        boss_invader.addcomponent(BOSS_INVADER_POLY, game_color)
        self.screen.register_shape("boss_invader", boss_invader)

    def register_health_4(self, game_color):
        health_4 = Shape("compound")
        health_4.addcomponent(HEALTH_4, game_color)
        self.screen.register_shape("health_4", health_4)

    def register_health_3(self, game_color):
        health_3 = Shape("compound")
        health_3.addcomponent(HEALTH_3, game_color)
        self.screen.register_shape("health_3", health_3)

    def register_health_2(self, game_color):
        health_2 = Shape("compound")
        health_2.addcomponent(HEALTH_2, game_color)
        self.screen.register_shape("health_2", health_2)

    def register_health_1(self, game_color):
        health_1 = Shape("compound")
        health_1.addcomponent(HEALTH_1, game_color)
        self.screen.register_shape("health_1", health_1)

    def register_explosion(self, game_color):
        explosion = Shape("compound")
        explosion.addcomponent(EXPLOSION_POLY, game_color)
        self.screen.register_shape("explosion", explosion)

    def register_small_explosion(self, game_color):
        small_explosion = Shape("compound")
        small_explosion.addcomponent(SMALL_EXPLOSION_POLY, game_color)
        self.screen.register_shape("small_explosion", small_explosion)

    def add_projectile(self, x_coord, y_coord, direction, speed, game_color):
        new_projectile = Projectile(x_coord, y_coord, direction, speed, game_color)
        self.all_projectiles.append(new_projectile)

    def move_projectiles(self):
        for projectile in self.all_projectiles:
            if -415 <= projectile.ycor() <= 550:
                projectile.move()
            else:
                self.destroy_projectile(projectile)

    def destroy_projectile(self, projectile):
        self.all_projectiles = [valid_projectile for valid_projectile in self.all_projectiles if
                                valid_projectile.id != projectile.id]
        projectile.destroy()

    def destroy_all_projectiles(self):
        for projectile in self.all_projectiles:
            projectile.destroy()
        self.all_projectiles = []

    def calc_game_speed(self):
        self.turns += 1
        if self.turns <= 300:
            return 10
        elif self.turns <= 600:
            return 6
        elif self.turns <= 1200:
            return 4
        else:
            return 2