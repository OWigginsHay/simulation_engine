from simeng.object import Object
from simeng.data_structs.cell import Cell
from simeng.data_containers import grid




class MovingPoint(Object):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def behaviour(self):
        self.x += 1
        self.y += 1

    def type(self):
        print(type(self).__name__)

if __name__ == '__main__':
    from simeng import Engine
    from simeng.data_containers.grid import Grid

    Engine(Grid).run()