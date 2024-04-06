from turtle import Turtle
from game_master import GameMaster

class BossInvader(Turtle, GameMaster):

    def __init__(self, game_color):
        super().__init__()
        self.penup()
        self.register_boss_invader(game_color)
        self.register_health_4(game_color)
        self.register_health_3(game_color)
        self.register_health_2(game_color)
        self.register_health_1(game_color)
        self.spawn(game_color)
        self.direction = 1
        self.speed = 4
        self.health = 4
        self.health_bar = Turtle()
        self.spawn_health_bar()

    def spawn(self, game_color):
        self.shape("boss_invader")
        self.setposition(-300, 600)
        self.setheading(90)

    def spawn_health_bar(self):
        self.health_bar.shape("health_4")
        self.health_bar.setposition(-300, 630)
        self.health_bar.setheading(90)

    def move(self):
        if self.ycor() > 450:
            new_y = self.ycor() - self.speed
            self.goto(self.xcor(), new_y)
            self.health_bar.goto(self.xcor(), new_y + 30)
        else:
            if self.xcor() >= 330:
                self.direction = -1
            elif self.xcor() <= -330:
                self.direction = 1
            elif -330 < self.xcor() < 330:
                pass

            new_x = self.xcor() + self.speed * self.direction
            self.goto(new_x, self.ycor())
            self.health_bar.goto(new_x, self.ycor() + 30)

    def handle_hit(self):
        self.health -= 1
        # self.destroy_health_bar()
        # self.health_bar = Turtle()
        if self.health == 3:
            self.health_bar.shape("health_3")
        elif self.health == 2:
            self.health_bar.shape("health_2")
        elif self.health == 1:
            self.health_bar.shape("health_1")
        elif self.health < 1:
            self.destroy()

    def destroy(self):
        self.hideturtle()
        self.clear()
        self.health_bar.hideturtle()
        self.health_bar.clear()