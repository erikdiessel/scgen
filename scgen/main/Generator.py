import pandas as pd

from scgen.main.Output import Outputter

import random

DEFAULT_SEED = 1717

class Generator:

    def __init__(self):
        self.__availableElements = {}
        self.__availableModules = {}
        self.__availableDistributions = {}

        self.__elementDict = dict()
        self.__moduleDict = dict()

    def registerElement(self, element):
        nameOfElement = element.name
        self.__availableElements[nameOfElement] = element

    def registerModule(self, module):
        nameOfModule = module.name
        self.__availableModules[nameOfModule] = module

    def registerDistribution(self, distribution):
        nameOfDistribution = distribution.name
        self.__availableDistributions[nameOfDistribution] = distribution

    def generate(self, settings):
        random.seed(DEFAULT_SEED)

        self.initializeSeed(settings)

        elements_settings = settings["elements"]
        self.generateElements(elements_settings)        
        modules_settings = settings["modules"]
        self.generateModules(modules_settings)
        return self.output()

    def initializeSeed(self, settings):
        if "seed" in settings:
            random.seed(settings["seed"])

    def generateElements(self, elements_settings):
        self.__elementDict = {
            setting["type"]:
            self.generateElement(setting) for setting in elements_settings
        }

    def generateElement(self, setting):
        elementType = setting["type"]
        elementComponent = self.__availableElements[elementType]
        instantiatedElements = elementComponent(**setting)
        return instantiatedElements

    def generateModules(self, modules_settings):
        # Generate iteratively since modules might depend on
        # previous modules
        
        for setting in modules_settings: 
            # choose the output name either as provided in the setting
            outputName = (setting["outputName"] 
                if "outputName" in setting else setting["type"])
            self.__moduleDict[outputName] = self.generateModule(setting)

    def generateModule(self, setting):
        moduleType = setting["type"]
        moduleComponent = self.__availableModules[moduleType]
        instantiatedModule = moduleComponent(
            elementList = self.__elementDict,
            moduleList = self.__moduleDict,
            distributionsProvider = self.__availableDistributions,
            **setting
        )

        return instantiatedModule

    def getElements(self):
        return [
            {
                "type": element.name,
                "members": element.members()
            }
            for element in self.__elementDict.values() 
        ]

    def getModuleValues(self):
        return {
            moduleName: self.__moduleDict[moduleName].getValues()
            for moduleName in self.__moduleDict.keys()    
        }

    def output(self):
        return Outputter(self.__elementDict, self.__moduleDict)