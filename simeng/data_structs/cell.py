from pyglet import shapes
import events

class MyEvents(events.Events):

    __events__ = ('on_this', 'on_that', )

class Cell:

    def __init__(self):
        self.square = shapes.Rectangle(x=200, y=200, width=200, height=200, color=(55, 55, 255))

    def draw(self):
        self.square.draw()

m = MyEvents()

def lol():
    print("spook")

m.on_this += lol
m.on_this()