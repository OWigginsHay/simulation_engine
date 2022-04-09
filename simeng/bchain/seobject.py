from __future__ import annotations
from typing import TYPE_CHECKING
import typing
import inspect

import pytest
if TYPE_CHECKING:
    from . import Container
    from ..graphics import SEShape
from enum import Enum
import pyglet

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

class SEObject:

    AppearanceConfiguration = AppearanceConfiguration

    def __init__(self, **init):
        self.owner: Container = None
        self.__shape_callback: typing.Callable[[dict]] = None

    def _logic(self):
        pass

    def _declare_variables(self) -> dict:
        return {}

    def _declare_appearance(self) -> dict:
        config = self.AppearanceConfiguration()
        return config

    def __update(self):
        self._logic()
        config = self._declare_appearance()
        self.__shape_callback(config)

    def update(self):
        self.__update()

    def attach_outlets(self, shape: SEShape):
        try:
            from ..graphics import SEShape
            assert issubclass(shape.__class__, SEShape)
        except AssertionError:
            for att in shape.__dir__():
                print(att, ": ", getattr(shape, att))
            raise
        self.__shape_callback = shape.update_appearance
