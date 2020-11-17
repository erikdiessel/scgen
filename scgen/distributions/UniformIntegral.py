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
        except ValueError as e:
            raise ValueError(f"The parameters min={self.__min}, max={self.__max} of the uniformIntegral distribution are invalid: {e}")