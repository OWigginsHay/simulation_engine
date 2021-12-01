import pyglet
from pyglet.canvas.base import Canvas
from event_handler import EventHandler

display = pyglet.canvas.get_display()
screen = display.get_default_screen()

window = pyglet.window.Window(style = pyglet.window.Window.WINDOW_STYLE_DEFAULT, caption = "League of Legends")
icon = pyglet.image.load('icon.png')
window.set_icon(icon)

event_handler = EventHandler(window)

#Debug
# event_logger = pyglet.window.event.WindowEventLogger()
# window.push_handlers(event_logger)

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    event_loop.exit()

@window.event
def on_draw():
    window.clear()
    label = pyglet.text.Label('x: {}, y: {}'.format(event_handler.mouse_pos['x'], event_handler.mouse_pos['y']),
                        font_name='Times New Roman',
                        font_size=36,
                        x=window.width//2, y=window.height//2,
                        anchor_x='center', anchor_y='center')
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    ('v2i', (10, 15, 30, 35)),
    ('c3B', (0, 0, 255, 0, 255, 0))
)
    label.draw()
    

pyglet.app.run()