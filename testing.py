from ast import Sub
import random
import typing
from enum import Enum
from typing import Dict
import numpy as np


class SEObject:

    def __init__(self):
        self.owner = None

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

class Container:

    def __init__(self, userType):
        self.of_type = userType.__name__
        self.spawn_type = userType
        self.children = []

    def make(self, n=1) -> typing.List[SEObject]:
        for _ in range(n):
            child = self.spawn_type()
            child.owner = self
            self.children.append(child)
            for other in self.children:
                other.x += random.random()
                other.y += random.random()
        return self.children

class Layer:

    def __init__(self):
        self.contains_types = dict()

    def attach(self, container: Container):
        if not container.of_type in self.contains_types:
            self.contains_types[container.of_type] = container
        else:
            print("Container of Type: {} already exists".format(container.of_type))

    def __getitem__(self, item) -> Container:
        return self.contains_types[item]

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

pub = Publisher(['lunch', 'dinner'])

bob = Subscriber("bob")
alice = Subscriber2("alice")
john = Subscriber("john")

pub.register('lunch', bob)
pub.register('lunch', alice, alice.recieve)
pub.register('dinner', john)

pub.dispatch('lunch', "Lunch time")
pub.dispatch('dinner', "Dinner time")
