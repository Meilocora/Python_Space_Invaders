from turtle import Screen
import time
import random

from defender import Defender
from screen_manager import ScreenManager
from game_master import GameMaster
from obstacle_manager import ObstacleManager
from invader_manager import InvaderManager
from boss_invader import BossInvader

# ========== CONSTANTS ========== #
WIDTH = 800
HEIGHT = 1000
GAME_COLORS = {
    "green": "#00FF00",
    "red": "#F41613",
    "blue": "#03F7F7",
    "yellow": "#F5F430",
    "pink": "#F70FE8",
    "white": "#FFFFFF",
    "random": f'#{random.randrange(256 ** 3):06x}'
}
GAME_COLOR = ''
# ========== SETTING ========== #

def choose_game_color():
    global GAME_COLOR
    chosen_color = input("Please choose a color: green, red, blue, yellow, pink, white, random\n").lower()
    if chosen_color in GAME_COLORS.keys():
        GAME_COLOR = GAME_COLORS[chosen_color]
    else:
        print(f'The color "{chosen_color}" is not a valid option...')
        choose_game_color()

choose_game_color()
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

defender = Defender(GAME_COLOR)
screen_manager = ScreenManager(GAME_COLOR)
game_master = GameMaster()
obstacle_manager = ObstacleManager(GAME_COLOR)
invader_manager = InvaderManager(GAME_COLOR)
# ========== INGAME CONTROLS ========== #
def defender_shoot():
    defender.shoot(game_master)

screen.listen()
screen.onkey(defender.go_right, "Right")
screen.onkey(defender.go_left, "Left")
screen.onkey(defender_shoot, "space")

# ========== GAME LOGIC ========== #
game_is_on = True
boss_invader = False
while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_speed = game_master.calc_game_speed()
    if game_master.turns == 1000:
        boss_invader = BossInvader(GAME_COLOR)
    game_master.move_projectiles()
    if boss_invader:
        invader_manager.handle_invaders(game_master, game_speed, boss_invader)
    else:
        invader_manager.handle_invaders(game_master, game_speed)
    screen_manager.calc_explosions()

    # Detect collision of projectile
    for projectile in game_master.all_projectiles:
        # Collision with Obstacle
        for obstacle in obstacle_manager.all_obstacles:
              # Collision from bottom
            if (obstacle.bottom["x"] - 4 <= projectile.xcor() <= obstacle.bottom["x"] + 4) and (obstacle.bottom["y"] - 5 <= projectile.ycor() <= obstacle.bottom["y"] + 5):
                screen_manager.set_explosion("small_explosion", projectile.xcor(), projectile.ycor())
                game_master.destroy_projectile(projectile)
                obstacle_manager.delete_obstacle(obstacle)

              # Collision from top
            if (obstacle.top["x"] - 4 <= projectile.xcor() <= obstacle.top["x"] + 4) and (obstacle.top["y"] - 5 <= projectile.ycor() <= obstacle.top["y"] + 5):
                screen_manager.set_explosion("small_explosion", projectile.xcor(), projectile.ycor())
                game_master.destroy_projectile(projectile)
                obstacle_manager.delete_obstacle(obstacle)

        # Collision with Invader
        for invader in invader_manager.all_invaders:
            if (invader.xcor() - 15  <= projectile.xcor() <= invader.xcor() + 15) and (invader.ycor() - 20 <= projectile.ycor() <= invader.ycor() - 10) and projectile.direction == 1:
                screen_manager.set_explosion("explosion", invader.xcor(), invader.ycor())
                game_master.destroy_projectile(projectile)
                invader_manager.delete_invader(invader)
                screen_manager.increase_score(25)

        # Collision with BossInvader
        if boss_invader:
            if (boss_invader.xcor() - 16 <= projectile.xcor() <= boss_invader.xcor() + 16) and (boss_invader.ycor() - 10 <= projectile.ycor() <= boss_invader.ycor()) and projectile.direction == 1:
                game_master.destroy_projectile(projectile)
                boss_invader.handle_hit()
                if boss_invader.health == 0:
                    screen_manager.set_explosion("explosion", boss_invader.xcor(), boss_invader.ycor())
                    screen_manager.increase_score(200)

        # Collision of with Defender
        if (defender.xcor() - 20 <= projectile.xcor() <= defender.xcor() + 20) and (defender.ycor() <= projectile.ycor() <= defender.ycor() + 26):
            screen_manager.set_explosion("explosion", defender.xcor(), defender.ycor())
            if defender.lifes == 0:
                game_master.destroy_all_projectiles()
                screen.update()
                if boss_invader:
                    screen_manager.game_over("lost", len(invader_manager.all_invaders), boss_invader.health, game_master.turns)
                else:
                    screen_manager.game_over("lost", len(invader_manager.all_invaders), 4, game_master.turns)
                game_is_on = False
            else:
                game_master.destroy_projectile(projectile)
                defender.respawn()
                screen_manager.loose_life()
                game_master.destroy_all_projectiles()

        # Collision of with other projectile
        for hit_projectile in game_master.all_projectiles:
            if (projectile.direction != hit_projectile.direction) and (hit_projectile.xcor() - 4 <= projectile.xcor() <= hit_projectile.xcor() + 4) and (hit_projectile.ycor() -10 <= projectile.ycor() <= hit_projectile.ycor() + 10):
                screen_manager.set_explosion("small_explosion", hit_projectile.xcor(), hit_projectile.ycor())
                game_master.destroy_projectile(projectile)
                game_master.destroy_projectile(hit_projectile)

        # Check if player won
        if boss_invader and boss_invader.health == 0 and len(invader_manager.all_invaders) == 0:
            game_master.destroy_all_projectiles()
            screen.update()
            screen_manager.game_over("won", len(invader_manager.all_invaders), 0, game_master.turns)
            game_is_on = False

screen.exitonclick()