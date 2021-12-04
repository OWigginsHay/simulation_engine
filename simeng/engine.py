from typing import Container
import pyglet
from pyglet.canvas.base import Canvas
from simeng.event_handler import EventHandler
from simeng.mainScene import MainScene
from simeng.data_containers.grid import Grid
from simeng.data_containers.container import Container
#Debug
# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

class Engine():

    def __init__(self, data: Container, width=600, height=400):
        self.display = pyglet.canvas.get_display()
        self.window = pyglet.window.Window(width, height, style = pyglet.window.Window.WINDOW_STYLE_DEFAULT, caption = "Simulation Engine")
        self.icon = pyglet.image.load('icon.png')
        self.window.set_icon(self.icon)
        self.event_handler = EventHandler(self.window)
        self.current_screen = MainScene(self, data, width=width, height=height)

    def run(self):
        event_loop = pyglet.app.EventLoop()

        @event_loop.event
        def on_window_close(window):
            event_loop.exit()

        pyglet.app.run()

if __name__ == '__main__':

    engine = Engine(Grid)
    engine.run()
