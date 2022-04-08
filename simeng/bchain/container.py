from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from simeng.bchain.seobject import SEObject

import typing
import random

class Container:

    def __init__(self, userType: typing.Type[SEObject]):
        self.of_type:str = userType.__name__
        self.spawn_type:typing.Callable[[dict], SEObject] = userType
        self.__children: typing.List[SEObject] = []

    def make(self, n=1) -> typing.List[SEObject]:
        args = []
        kwargs = {}
        for _ in range(n):
            child = self.spawn_type(*args, **kwargs)
            child.owner = self
            self.__children.append(child)
        return self.__children

    def get_children(self):
        return self.__children

    def update(self):
        for child in self.__children:
            child.update()

    def get_closest(self, obj: SEObject):
        if obj.__class__.__name__ in self.of_type:
            print("yes")