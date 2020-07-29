from scgen.base_components.Distribution import Distribution

from random import randint

class UniformIntegral(Distribution):
    name = "uniformIntegral"

    def __init__(self, min, max, **additionalSettings):
        self.__min = min
        self.__max = max

    def generate(self):
        try: 
            return randint(self.__min, self.__max)
        except ValueError:
            raise ValueError(f"The parameters of the uniformIntegral-distribution are invalid: min: {self.min}, max: {self.max}")