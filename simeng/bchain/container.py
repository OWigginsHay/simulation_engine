from __future__ import annotations
from typing import TYPE_CHECKING
# if TYPE_CHECKING:
#     from .seobject import SEObject

import typing

class Container:

    def __init__(self, userType: typing.Type[SEObject]):
        self.of_type:str = userType.__name__
        self.spawn_type:typing.Callable[[dict], SEObject] = userType
        self.__children: typing.List[SEObject] = []

    def make(self, n=1) -> typing.List[SEObject]:
        args = []
        kwargs = {'owner': self}
        self.__children = [self.spawn_type(*args, **kwargs) for _ in range(n)]
        return self.__children

    def get_children(self):
        return self.__children

    def update(self):
        for child in self.__children:
            child.update()

    def get_closest(self, obj: SEObject):
        pass
        # if obj.__class__.__name__ in self.of_type:
        #     for child in self.__children:
        #         pass
