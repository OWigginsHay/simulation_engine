from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from simeng.bchain.seobject import SEObject

import typing
import random

class Container:

    def __init__(self, userType):
        self.of_type = userType.__name__
        self.spawn_type = userType
        self.children: typing.List[SEObject] = []

    def make(self, n=1) -> typing.List[SEObject]:
        for _ in range(n):
            child = self.spawn_type()
            child.owner = self
            self.children.append(child)
        return self.children

    def draw(self):
        for child in self.children:
            child.update()