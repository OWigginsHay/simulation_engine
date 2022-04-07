from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from simeng.bchain import SEObject

from pyglet.graphics import Batch
from pyglet import shapes
from simeng.graphics import Shape, Circle
import random


class ShapeContainer:

    def __init__(self):
        self.batch = Batch()
        self.shapes = []

    def make_shape(self):
        shape = Circle(batch=self.batch)
        return shape

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)

    def remove_shape(self, shape: Shape):
        self.shapes.remove(shape)

    def link_to_object(self, object: SEObject):
        shape = self.make_shape()
        object.attach_outlets(shape)
        #Get exposed outputs of SEObject
        #Get shape to observe those perameters 
        #Define a kill function
        self.add_shape(shape)

    def draw(self):
        for shape in self.shapes:
            shape.shape.draw()
