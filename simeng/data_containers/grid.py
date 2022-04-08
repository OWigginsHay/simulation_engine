from typing import Container
import pyglet
from simeng.data_containers.container import DataContainer

class Grid(DataContainer):

    def __init__(self, x, y, width=10, height=10):
        self.x = x
        self.y = y
        self.batch = pyglet.graphics.Batch()
        self.dimension = min(width//x, height//y)

    def update(self):
        self.batch.draw()

    def at_x_y(self, x, y, element):
        pass
