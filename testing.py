from ast import Sub
import random
import typing
from enum import Enum
from typing import Dict
import numpy as np
from simeng.bchain import *

class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print("{} got message: {}".format(self.name, message))

class Subscriber2:
    def __init__(self, name):
        self.name = name

    def recieve(self, message):
        print("{} got message: {}".format(self.name, message))

class Publisher:
    def __init__(self, events):
        self.subscribers = {event : dict() 
                            for event in events}
    def get_subscribers(self, event):
        return self.subscribers[event]
    def register(self, event, who, callback=None):
        if callback is None:
            callback = getattr(who, "update")
        self.get_subscribers(event=event)[who] = callback
    def unregister(self, event, who):
        del self.get_subscribers(event)[who]
    def dispatch(self, event, message):
        for _, callback in self.get_subscribers(event).items():
            callback(message)


class Point(SEObject):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def exposeOutputs(self):
        return {
            'x':self.x, 
            'y':self.y,
            }

l = Layer()
l.attach(Container(Point))
l['Point'].make(10)[0].owner



# pub = Publisher(['lunch', 'dinner'])

# bob = Subscriber("bob")
# alice = Subscriber2("alice")
# john = Subscriber("john")

# pub.register('lunch', bob)
# pub.register('lunch', alice, alice.recieve)
# pub.register('dinner', john)

# pub.dispatch('lunch', "Lunch time")
# pub.dispatch('dinner', "Dinner time")
