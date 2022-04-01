from pyglet import shapes

class Cell:

    def __init__(self, x=0, y=0, width=100, height=100, color=(255, 255, 255), batch=None):
        self.square = shapes.Rectangle(x=x, y=y, width=width, height=height, color=color, batch=batch)

    def draw(self):
        self.square.draw()

def lol():
    print("spook")
