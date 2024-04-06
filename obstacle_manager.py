from obstacle import Obstacle
import numpy as np


class ObstacleManager():
    def __init__(self, game_color):
        self.all_obstacles = []
        self.game_color = game_color
        self.create_obstacles()


    def create_obstacles(self):
        obstacle_id = 0
        x_coords = np.arange(-100 * np.pi, 100 * np.pi, 10)
        for num in range(-100, 100, 100):
            y_coords = (np.sin(10*x_coords)*30)+num
            for x, y in zip(x_coords, y_coords):
                new_obstacle = Obstacle(self.game_color, round(x), round(y), obstacle_id)
                obstacle_id += 1
                self.all_obstacles.append(new_obstacle)

    def delete_obstacle(self, obstacle):
        self.all_obstacles = [valid_obstacle for valid_obstacle in self.all_obstacles if valid_obstacle.id != obstacle.id]
        obstacle.destroy()