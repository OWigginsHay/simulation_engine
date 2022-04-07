from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..graphics import Shape

class SEObject:

    def __init__(self):
        self.owner = None
        self.shape_callback = None

    def logic(self):
        pass

    def update(self):
        self.logic()
        state = self.declare_variables()
        self.shape_callback(state)

    def declare_variables(self) -> dict:
        return {}

    def expose_outlets(self):
        #return a dictionary mapping keys to instance members
        self.shape_callback(self.declare_variables())
        pass

    def attach_outlets(self, shape: Shape):
        self.shape_callback = shape.update_state