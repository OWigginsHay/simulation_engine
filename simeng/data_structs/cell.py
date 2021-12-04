from pyglet import shapes
import events

class MyEvents(events.Events):

    __events__ = ('on_this', 'on_that', )

class Cell:

    def __init__(self, x=0, y=0, width=100, height=100, color=(255, 255, 255), batch=None):
        self.square = shapes.Rectangle(x=x, y=y, width=width, height=height, color=color, batch=batch)

    def draw(self):
        self.square.draw()

m = MyEvents()

def lol():
    print("spook")

m.on_this += lol
m.on_this()