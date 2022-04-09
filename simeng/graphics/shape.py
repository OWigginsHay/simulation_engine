from __future__ import annotations
from turtle import width
from typing import TYPE_CHECKING

from simeng.bchain.seobject import Shapes

if TYPE_CHECKING:
    from simeng.bchain import SEObject
    from simeng.bchain.seobject import AppearanceConfiguration

from ..bchain.seobject import Shapes
from enum import Enum

class SEShape:

    def __init__(self, batch=None):
        pass

    def update_state(self, dic):
        pass

    def listen_to_object(self, object: SEObject):
        object.attach_outlets()

    def update_appearance(self, config: AppearanceConfiguration):
        self.shape.x = config.x
        self.shape.y = config.y



class SECircle(SEShape):

    def __init__(self, batch=None, **kwargs):
        print("Gonna make a circle")
        shape_class = Shapes.CIRCLE.value
        print(kwargs)
        self.shape = shape_class(
            x=kwargs.get('x'), 
            y=kwargs.get('y'), 
            radius=kwargs.get('radius'),
            color=(kwargs.get('colour')),
            batch=batch
            )

    def listen_to_object(self, object: SEObject):
        object.attach_outlets()

    def update_state(self, state):
        pass

    def update_appearance(self, config: AppearanceConfiguration):
        self.shape.x = config.x
        self.shape.y = config.y


class SESquare(SEShape):

    def __init__(self, batch=None, **kwargs):
        print("Gonna make a square")
        self.shape = Shapes.RECTANGLE.value(
            x=kwargs.get('x'),
            y=kwargs.get('y'),
            width=kwargs.get('width'),
            height=kwargs.get('width'),
            color=(kwargs.get('colour')),
            batch=batch)

    def listen_to_object(self, object: SEObject):
        object.attach_outlets()

    def update_state(self, state):
        pass

    def update_appearance(self, config: AppearanceConfiguration):
        self.shape.x = config.x
        self.shape.y = config.y

class ShapeFactory:

    shape_options = {
        Shapes.CIRCLE.name: SECircle,
        Shapes.SQUARE.name: SESquare,
    }

    def __init__(self):
        pass

    @classmethod
    def make_shape(cls, batch, config:AppearanceConfiguration):
        obj = cls.shape_options[config.shape.name](batch=batch, **vars(config))
        return obj
