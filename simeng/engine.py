import pyglet
from pyglet.canvas.base import Canvas
from simeng.event_handler import EventHandler
from simeng.mainScene import MainScene
from simeng.data_containers.grid import Grid
from simeng.data_containers.container import DataContainer
from simeng.graphics.shapeContainer import ShapeContainer
from simeng.bchain import *
import random

class Test(SEObject):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def logic(self):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)

    def declare_variables(self):
        print("declared")
        return {"x":self.x,"y":self.y}
#Debug
# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

class Engine():

    def __init__(self, data: DataContainer, width=600, height=400):
        self.display = pyglet.canvas.get_display()
        self.window: pyglet.window.Window = pyglet.window.Window(width, height, style = pyglet.window.Window.WINDOW_STYLE_DEFAULT, caption = "Simulation Engine")
        self.icon = pyglet.image.load('icon.png')
        self.window.set_icon(self.icon)
        self.event_handler = EventHandler(self.window)
        
        self.sc = ShapeContainer()
        for _ in range(10):
            self.sc.add_shape(self.sc.make_shape())
        self.sc.draw()
        self.current_screen = MainScene(self, data, width=width, height=height, tmpsc=self.sc)

    def initialize_layer(self, layer: Layer):
        for item in layer.contains_types.items():
            for child in item[1].children:
                self.sc.link_to_object(child)
        #self.window.set_handler('on_draw', self.sc.draw)
        self.window.set_handler('on_draw', layer.draw)

    def update(self, dt):
        pass

    def run(self):
        event_loop = pyglet.app.EventLoop()
        @event_loop.event
        def on_window_close(window):
            event_loop.exit()
        pyglet.app.run()
        pyglet.clock.schedule_interval(self.update, 1/30)

if __name__ == '__main__':

    l = Layer()
    c = Container(Test)
    l.attach(c)
    l['Test'].make(2)

    engine = Engine(Grid)
    engine.initialize_layer(l)
    print(engine.sc.shapes)
    engine.run()