from scgen.base_components.Distribution import Distribution

from random import uniform

class Bernoulli(Distribution):
    name = "bernoulli"

    def __init__(self, probability, **additionalSettings):
        self.__probability = probability

    def generate(self):
        return 1 if uniform(0,1) <= self.__probability else 0