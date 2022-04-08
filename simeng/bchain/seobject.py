from __future__ import annotations
from typing import TYPE_CHECKING
import typing
if TYPE_CHECKING:
    from ..graphics import Shape
    from . import Container

class SEObject:

    def __init__(self, **init):
        self.owner:Container = None
        self.__shape_callback:typing.Callable[[dict]] = None

    def _logic(self):
        pass

    def _declare_variables(self) -> dict:
        return {}

    def __update(self):
        self._logic()
        state = self._declare_variables()
        self.__shape_callback(state)

    def update(self):
        self.__update()

    def attach_outlets(self, shape: Shape):
        self.__shape_callback = shape.update_state
