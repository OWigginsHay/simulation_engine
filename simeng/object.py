from abc import ABC, abstractmethod

class Object(ABC):

    @abstractmethod
    def behaviour(self):
        pass