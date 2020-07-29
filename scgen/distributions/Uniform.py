from scgen.base_components.Distribution import Distribution

from random import uniform

class Uniform(Distribution):
    name = "uniform"

    def __init__(self, min, max, **additionalSettings):
        self.__min = min
        self.__max = max

    def generate(self):
        return uniform(self.__min, self.__max)