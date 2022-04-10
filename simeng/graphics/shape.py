from __future__ import annotations
import pyglet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simeng.bchain import SEObject
    from pyglet.shapes import _ShapeBase

from enum import Enum

class Shapes(Enum):
    CIRCLE = pyglet.shapes.Circle
    SQUARE = pyglet.shapes.Rectangle
    RECTANGLE = pyglet.shapes.Rectangle
    ELLIPSE = pyglet.shapes.Ellipse
    LINE = pyglet.shapes.Line
    BORDER_RECTANGLE = pyglet.shapes.BorderedRectangle
    TRIANGLE = pyglet.shapes.Triangle

class AppearanceConfiguration:

    Shapes = Shapes

    def __init__(self):
        self.shape: Shapes = Shapes.CIRCLE
        self.x: int = 0
        self.y: int = 0
        self.visible: bool = True
        self.colour = (255, 255, 255)
        self.opacity: int = 255
        self.radius = 0
        #Ellipses
        self.a = 0
        self.b = 0
        #Rectangle
        self.height: int = 0
        self.width: int = 0
        #Lines
        self.x2: int = 0
        self.y2: int = 0

class _SEShape:

    def __init__(self, batch=None):
        self.shape: _ShapeBase

    def update_state(self, dic):
        pass

    def listen_to_object(self, object: SEObject):
        object.attach_outlets()

    def update_appearance(self, config: AppearanceConfiguration):
        self.shape.x = config.x
        self.shape.y = config.y

    def reveal_shape_dict(self):
        print(vars(self.shape))

class SECircle(_SEShape):

    def __init__(self, batch=None, **kwargs):
        super().__init__()
        shape_class = Shapes.CIRCLE.value
        self.shape = shape_class(
            x=kwargs.get('x'), 
            y=kwargs.get('y'), 
            radius=kwargs.get('radius'),
            color=(kwargs.get('colour')),
            batch=batch
            )

class SERectangle(_SEShape):

    def __init__(self, batch=None, **kwargs):
        super().__init__()
        self.shape = Shapes.RECTANGLE.value(
            x=kwargs.get('x'),
            y=kwargs.get('y'),
            width=kwargs.get('width'),
            height=kwargs.get('height'),
            color=(kwargs.get('colour')),
            batch=batch)

class SESquare(_SEShape):

    def __init__(self, batch=None, **kwargs):
        super().__init__()
        self.shape = Shapes.RECTANGLE.value(
            x=kwargs.get('x'),
            y=kwargs.get('y'),
            width=kwargs.get('width'),
            height=kwargs.get('width'),
            color=(kwargs.get('colour')),
            batch=batch)

class SEEllipse(_SEShape):

    def __init__(self, batch=None, **kwargs):
        super().__init__()
        self.shape = Shapes.RECTANGLE.value(
            x=kwargs.get('x'),
            y=kwargs.get('y'),
            width=kwargs.get('width'),
            height=kwargs.get('height'),
            color=(kwargs.get('colour')),
            batch=batch)

class ShapeFactory:

    shape_options = {
        Shapes.CIRCLE.name: SECircle,
        Shapes.SQUARE.name: SESquare,
    }

    @classmethod
    def make_shape(cls, batch, config:AppearanceConfiguration):
        obj = cls.shape_options[config.shape.name](batch=batch, **vars(config))
        return obj
