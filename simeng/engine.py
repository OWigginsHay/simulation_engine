import pyglet
from pyglet.canvas.base import Canvas
from event_handler import EventHandler
from mainScene import MainScene

#Debug
# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

class Engine():

    def __init__(self):
        self.display = pyglet.canvas.get_display()
        self.window = pyglet.window.Window(style = pyglet.window.Window.WINDOW_STYLE_DEFAULT, caption = "Simulation Engine")
        self.icon = pyglet.image.load('icon.png')
        self.window.set_icon(self.icon)
        self.event_handler = EventHandler(self.window)
        self.current_screen = MainScene(self)

engine = Engine()

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    event_loop.exit()

pyglet.app.run()