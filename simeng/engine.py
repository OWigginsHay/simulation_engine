import pyglet
from simeng.event_handler import EventHandler
from simeng.graphics.shapeContainer import ShapeContainer
from simeng.bchain import *

class Engine():

    def __init__(self, width=1200, height=800):
        self.display = pyglet.canvas.get_display()
        config = pyglet.gl.Config()
        config.sample_buffers = 1
        config.samples = 8
        self.window: pyglet.window.Window = pyglet.window.Window(width, height, style = pyglet.window.Window.WINDOW_STYLE_DEFAULT, caption = "Simulation Engine")
        self.icon = pyglet.image.load('icon.png')
        self.window.set_icon(self.icon)
        self.event_handler = EventHandler(self.window)
        
        self.sc = ShapeContainer()
        self.layer = None

    def initialize_layer(self, layer: Layer):
        for item in layer.contains_types.items():
            for child in item[1].get_children():
                self.sc.link_to_object(child)
        self.layer = layer
        self.window.set_handler('on_draw', self.draw)
        
    def draw(self):
        self.window.clear()
        self.sc.draw()

    def update(self, dt):
        self.layer.update()

    def run(self):
        event_loop = pyglet.app.EventLoop()
        @event_loop.event
        def on_window_close(window):
            event_loop.exit()
        pyglet.clock.schedule_interval(self.update, 1/240)
        pyglet.app.run()
