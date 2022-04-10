from __future__ import annotations
from typing import TYPE_CHECKING
import typing
# if TYPE_CHECKING:
#     from . import Container

class Layer:

    def __init__(self):
        self.contains_types:typing.Dict[str, Container] = dict()

    def attach(self, container: Container):
        if not container.of_type in self.contains_types:
            self.contains_types[container.of_type] = container
        else:
            print("Container of Type: {} already exists".format(container.of_type))

    def __getitem__(self, item) -> Container:
        return self.contains_types[item]

    def update(self):
        for item in self.contains_types.items():
            item[1].update()