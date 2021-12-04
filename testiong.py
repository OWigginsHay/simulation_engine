import simeng as se
from simeng.engine import Engine
from simeng.object import Object
from simeng.data_structs.cell import Cell

class MovingPoint(Object):

    def __init__(self):
        self.x = 0
        self.y = 0

    def behaviour(self):
        self.x += 1
        self.y += 1


Engine().run()
m = MovingPoint()
m.behaviour()
print(m.x)