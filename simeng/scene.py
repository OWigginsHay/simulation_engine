class Scene(object):
    def __init__(self, canvas):
        self.window = canvas.window

    def start(self):
        self.window.set_handler('on_draw', self.on_draw)

    def clear():
        pass
