from simeng.bchain import *
import random

class Test(SEObject):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def update(self):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)

    def declare_variables(self):
        return {"x":self.x,"y":self.y}


l = Layer()
c = Container(Test)
#c.make(10)
l.attach(c)
l['Test'].make(10)