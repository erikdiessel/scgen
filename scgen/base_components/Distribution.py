from abc import ABCMeta, abstractmethod

class Distribution(metaclass=ABCMeta):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def generate(self):
        pass
