from __future__ import annotations
from typing import TYPE_CHECKING
import typing
from simeng.bchain import SEObject
from simeng.graphics.shape import ShapeFactory
if TYPE_CHECKING:
    from simeng.bchain.seobject import AppearanceConfiguration

from pyglet.graphics import Batch
from pyglet import shapes
from simeng.graphics import SEShape, SECircle
import random


class ShapeContainer:

    def __init__(self):
        self.batch = Batch()
        self.shapes: typing.List[SEShape] = []

    def make_shape(self, config: AppearanceConfiguration):
        shape = ShapeFactory.make_shape(batch=self.batch, config=config)
        return shape

    def add_shape(self, shape: SEShape):
        self.shapes.append(shape)

    def remove_shape(self, shape: SEShape):
        self.shapes.remove(shape)

    def link_to_object(self, seobject: SEObject):
        try:
            assert issubclass(seobject.__class__, SEObject)
        except AssertionError:
            for att in seobject.__dir__():
                print(att, ": ", getattr(seobject, att))
            raise
        shape = self.make_shape(seobject._declare_appearance())
        seobject.attach_outlets(shape)
        #Get exposed outputs of SEObject
        #Get shape to observe those perameters 
        #Define a kill function
        self.add_shape(shape)

    def draw(self):
        for shape in self.shapes:
            shape.shape.draw()
