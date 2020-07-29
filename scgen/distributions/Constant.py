from scgen.base_components.Distribution import Distribution

class Constant(Distribution):
    name = "constant"

    def __init__(self, value, **additionalSettings):
        self.__value = value

    def generate(self):
        return self.__value