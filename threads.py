import concurrent.futures as cf
import multiprocessing as mp
import random
exec = cf.Executor

r1 =[]
r2 = []

class Printer:
    def __init__(self):
        self.num = 0

    def do(self):
        self.num += 1

class Holder:

    def __init__(self):
        self.items = [Printer() for _ in range (1000000)]
        self.m = mp.Manager()
        self.p = mp.Pool(4)

    def run(self):
        self.p.map(self.do, self.items)
        # for item in self.items:
        #     item.do()

    def do(self, item):
        item.do()

    def kill(self):
        del self.m
        self.p.close()


def fun(a):
    # to show that the dictionaries are different
    a["1"] = random.random()

if __name__ == "__main__":

    h = Holder()
    h.run()
    del h
    # m = mp.Manager()
    # p = mp.Pool(4)
    # multi = [m.dict() for _ in range(10)]
    # p.map(fun, multi)
    # data = [a["1"] for a in multi]
    # print(data)
