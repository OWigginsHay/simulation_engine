from __future__ import annotations
from ..graphics import AppearanceConfiguration
from typing import TYPE_CHECKING
import typing

# if TYPE_CHECKING:
#     from . import Container
#     from ..graphics import _SEShape

class SEObject:

    AppearanceConfiguration = AppearanceConfiguration

    def __init__(self, *args, **init):
        self.owner: Container = init.get('owner')
        self.__shape_callback: typing.Callable[[dict]] = None

    def _logic(self):
        pass

    def _declare_appearance(self) -> dict:
        config = self.AppearanceConfiguration()
        return config

    def __update(self):
        self._logic()
        config = self._declare_appearance()
        self.__shape_callback(config)

    def update(self):
        self.__update()

    def attach_outlets(self, shape: _SEShape):
        try:
            from ..graphics import _SEShape
            assert issubclass(shape.__class__, _SEShape)
        except AssertionError:
            for att in shape.__dir__():
                print(att, ": ", getattr(shape, att))
            raise
        self.__shape_callback = shape.update_appearance
