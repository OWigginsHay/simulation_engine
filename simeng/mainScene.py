#from simeng.scene import Scene
import pyglet

class MainScene:

    def __init__(self, canvas, data, width, height, tmpsc):
        self.canvas = canvas
        self.window = canvas.window
        self.event_handler = canvas.event_handler
        self.data = data(6, 6, width=width, height=height)
        self.tmpsc = tmpsc
        self.start()

    def start(self):
        self.window.set_handler('on_draw', self.on_draw)

    def on_draw(self):
        self.window.clear()
        label = pyglet.text.Label('x: {}, y: {}'.format(self.event_handler.mouse_pos['x'], self.event_handler.mouse_pos['y']),
            font_name='Times New Roman',
            font_size=36,
            x=self.window.width//2, y=self.window.height//2,
            anchor_x='center', anchor_y='center')
        label.draw()
        self.tmpsc.draw()
