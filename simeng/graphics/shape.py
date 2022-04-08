from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from simeng.bchain import SEObject

from pyglet import shapes

class Shape:

    def __init__(self, batch=None):
        pass

    def update_state(self, dic):
        pass

class Circle:

    def __init__(self, batch=None):
        self.shape = shapes.Circle(x=0, y=0, radius=30, color=(200, 200, 200), batch=batch)

    def listen_to_object(self, object: SEObject):
        object.attach_outlets()

    def update_state(self, state):
        self.shape.x = state['x']
        self.shape.y = state['y']
        self.shape.color = state['colour']
        #print(state['x'], state['y'], sep=" ")