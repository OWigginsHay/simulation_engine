from typing import Container
import pyglet
from simeng.data_structs.cell import Cell
from simeng.data_containers.container import DataContainer

class Grid(DataContainer):

    def __init__(self, x, y, width=10, height=10):
        self.x = x
        self.y = y
        self.batch = pyglet.graphics.Batch()
        self.dimension = min(width//x, height//y)
        print(self.dimension)
        self.grid_elements = {
            '{},{}'.format(dx, dy):
            Cell(x=dx*self.dimension,
                 y=dy*self.dimension,
                 width=self.dimension,
                 height=self.dimension,
                 color=(100, dx*40, dy*40),
                 batch=self.batch) for dx in range(x) for dy in range(y)
        }

    def update(self):
        for x in range(self.x):
            for y in range(self.y):
                self.at_x_y(x, y, self.grid_elements['{},{}'.format(x, y)])
        self.batch.draw()

    def at_x_y(self, x, y, element):
        pass
