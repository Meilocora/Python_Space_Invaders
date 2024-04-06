from turtle import Turtle

class Obstacle(Turtle):

    def __init__(self, game_color, x_pos, y_pos, id):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setposition(x=x_pos, y=y_pos)
        self.color(game_color)
        self.shapesize(stretch_len=0.15, stretch_wid=3.5) # Default size 20px
        self.id = id
        self.bottom = {"x": x_pos, "y": y_pos-35}
        self.top = {"x": x_pos, "y": y_pos+35}

    def destroy(self):
        self.hideturtle()
        self.clear()
