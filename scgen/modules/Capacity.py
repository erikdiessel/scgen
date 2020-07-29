from scgen.base_components.Module import Module
from scgen.helpers.JointGeneration import generateJointly
from scgen.helpers.ForElements import hasAllElements

import pandas as pd

class Capacity(Module):
    """Provides a capacity limit on the full time horizon (as a sum) """

    name = "capacity"

    def __init__(self, forElements, distributions, elementList, moduleList, distributionsProvider, **additionalSettings):
        self.__forElements = forElements

        self.checkForRequirement("demand", moduleList)
        self.checkForRequirement("allocation", moduleList)       

        additionalCapacity = generateJointly(
            forElements = forElements,
            distributionSettings = distributions,
            elementList = elementList,
            distributionsProvider = distributionsProvider
        ).rename(columns = {"_value": "additionalCapacity"})

        if not hasAllElements(moduleList["allocation"].forElements(), of = forElements):
            raise ValueError("The allocation needs to have all keys that appear also in the capacity")

        allocation = moduleList["allocation"].getValues()

        # the capacity needed so that the allocation is just feasible
        minimalCapacity = allocation.groupby(
            forElements, as_index = False
        ).sum(
        ).rename(
            columns = { "allocation": "minimalCapacity" }    
        )
        
        self.__values = pd.merge(
            minimalCapacity, 
            additionalCapacity
        ).assign(
            capacity = lambda df: df["minimalCapacity"] + df["additionalCapacity"]
        ).drop(
            columns = ["minimalCapacity", "additionalCapacity"]        
        )

            
    def forElements(self):
        return self.__forElements

    def getValues(self):
        return self.__values