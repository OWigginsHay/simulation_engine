
import random
import pyglet
from simeng.bchain import *
from simeng.data_containers import Grid
from simeng import Engine

class Food(SEObject):

    def __init__(self):
        self.energy = 10
        self.x = random.randint(0, 800)
        self.y = random.randint(0,800)

    def _logic(self):
        pass

    def _declare_appearance(self) -> dict:
        config = self.AppearanceConfiguration()
        config.shape = config.Shapes.SQUARE
        config.x = self.x
        config.y = self.y
        config.width = 20
        config.colour = (0, 255, 0)
        return config


#Define some object with behaviour
class Test(SEObject):

    def __init__(self, **init):
        super().__init__(**init)
        self.velocityx = 0
        self.velocityy = 0
        self.x = 400
        self.y = 400
        self.delta = 1/120

        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)

    def _logic(self):
        self.velocityx += 40*(random.random()-.5)*self.delta
        self.velocityy += 40*(random.random()-.5)*self.delta
        self.x += self.velocityx*self.delta
        self.y += self.velocityy*self.delta
        self.owner.get_closest(self)

    def _declare_variables(self):
        #print("declared")
        return {"x": self.x, "y": self.y, "colour":(self.r, self.g, self.b)}

    def _declare_appearance(self) -> dict:
        config = self.AppearanceConfiguration()
        config.shape = config.Shapes.CIRCLE
        config.colour = (self.r, self.g, self.b)
        config.x = self.x
        config.y = self.y
        config.radius = 30
        return config


#Define Structure 
layer = Layer()
container = Container(Test)
container.make(10)
food_container = Container(Food)
food_container.make(40)
layer.attach(food_container)
layer.attach(container)

#Init and provide data to Engine
engine = Engine(Grid)
engine.initialize_layer(layer)
engine.run()
