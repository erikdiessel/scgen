from scgen.base_components.Module import Module
from scgen.helpers.JointGeneration import generateJointly

class BaseModule(Module):
    def __init__(self, forElements, distributions, elementList, moduleList, distributionsProvider, **additionalSettings):
        self.__forElements = forElements

        self.__values = generateJointly(
            forElements = forElements,
            distributionSettings = distributions,
            elementList = elementList,
            distributionsProvider = distributionsProvider
       )

    def forElements(self):
        return self.__forElements

    def getValues(self):
        return self.__values.rename(
            columns = {"_value": self.name}
        )