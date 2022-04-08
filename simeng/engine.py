import pyglet
import simeng
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
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)

    def declare_variables(self):
        #print("declared")
        return {"x":self.x,"y":self.y}
#Debug
# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

class Engine():

    def __init__(self, data: DataContainer, width=1200, height=800):
        self.display = pyglet.canvas.get_display()
        config = pyglet.gl.Config()
        config.sample_buffers = 1
        config.samples = 8
        self.window: pyglet.window.Window = pyglet.window.Window(width, height, style = pyglet.window.Window.WINDOW_STYLE_DEFAULT, caption = "Simulation Engine", config=config)
        self.icon = pyglet.image.load('icon.png')
        self.window.set_icon(self.icon)
        self.event_handler = EventHandler(self.window)
        
        self.sc = ShapeContainer()
        self.sc.draw()
        self.current_screen = MainScene(self, data, width=width, height=height, tmpsc=self.sc)
        self.layer = None

    def initialize_layer(self, layer: Layer):
        for item in layer.contains_types.items():
            for child in item[1].get_children():
                self.sc.link_to_object(child)
        self.layer = layer
        #self.window.set_handler('on_draw', self.sc.draw)
        

    def update(self, dt):
        self.layer.update()

    def run(self):
        event_loop = pyglet.app.EventLoop()
        @event_loop.event
        def on_window_close(window):
            event_loop.exit()
        pyglet.clock.schedule_interval(self.update, 1/240)
        pyglet.app.run()
        pyglet.clock.schedule_interval(self.update, 1/30)

if __name__ == '__main__':

    l = Layer()
    c = Container(Test)
    c.make(2)
    l.attach(c)

    

    engine = Engine(Grid)
    engine.initialize_layer(l)
    engine.run()
