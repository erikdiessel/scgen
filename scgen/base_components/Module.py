from abc import ABCMeta, abstractmethod

class Module(metaclass=ABCMeta):
	
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def getValues(self):
        pass

    @abstractmethod
    def forElements(self):
        pass

    def checkForRequirement(self, requirement, moduleList):
        if requirement not in moduleList:
            raise ValueError(
                f"The module {self.name} requires a {requirement} module initialized before"
            )