class EventHandler():

    def __init__(self, window):
        self.window = window
        self.mouse_pos = {
                'x':0,
                'y':0
            }

        @self.window.event
        def on_key_press(symbol, modifiers):
            pass

        @self.window.event
        def on_mouse_press(x, y, button, modifiers):
            self.mouse_pos['x'] = x
            self.mouse_pos['y'] = y

        @self.window.event
        def on_mouse_motion(x, y, dx, dy):
            self.mouse_pos['x'] = x
            self.mouse_pos['y'] = y

        @self.window.event
        def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
            self.mouse_pos['x'] = x
            self.mouse_pos['y'] = y