from __future__ import annotations
from typing import TYPE_CHECKING
import typing
from simeng.bchain import SEObject
from simeng.graphics.shape import ShapeFactory
# if TYPE_CHECKING:
#     from simeng.bchain.seobject import AppearanceConfiguration
#     from .shape import _SEShape

from pyglet.graphics import Batch


class ShapeContainer:

    def __init__(self):
        self.batch = Batch()
        self.shapes: typing.List[_SEShape] = []

    def make_shape(self, config: AppearanceConfiguration):
        shape = ShapeFactory.make_shape(batch=self.batch, config=config)
        return shape

    def add_shape(self, shape: _SEShape):
        self.shapes.append(shape)

    def remove_shape(self, shape: _SEShape):
        self.shapes.remove(shape)

    def link_to_object(self, seobject: SEObject):
        shape = self.make_shape(seobject._declare_appearance())
        seobject.attach_outlets(shape)
        self.add_shape(shape)

    def draw(self):
        self.batch.draw()
