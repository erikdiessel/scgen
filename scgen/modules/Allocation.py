from scgen.base_components.Module import Module
from scgen.helpers.JointGeneration import generateJointly

import pandas as pd

class Allocation(Module):
    name = "allocation"

    def __init__(self, forElements, distributions, elementList, moduleList, distributionsProvider, **additionalSettings):
        self.__forElements = forElements

        self.checkForRequirement("demand", moduleList)
        self.checkForRequirement("arc", moduleList)

        allWeights = generateJointly(
            forElements = forElements,
            distributionSettings = distributions,
            elementList = elementList,
            distributionsProvider = distributionsProvider
        ).rename(columns = {"_value": "_weight"})

        # Filter to only the existing arcs
        arc = moduleList["arc"].getValues()
        weightArcs = pd.merge(allWeights, arc)
        filteredWeights = weightArcs[weightArcs.existing == 1]

        demandElements = moduleList["demand"].forElements()
        weightSumsFiltered = (
            filteredWeights
            .groupby(demandElements, as_index = False)
            .sum()
            .rename(columns = { "_weight": "_weightSum" })
            .drop(columns = ["existing"])
        )

        weightsAndSums = pd.merge(weightArcs, weightSumsFiltered)

        combined = pd.merge(weightsAndSums, moduleList["demand"].getValues())
        
        self.__values = combined.assign(
                allocation = lambda df: df["existing"] * df["_weight"] / df["_weightSum"] * df["demand"]
            ).drop(
                columns = ['_weight', '_weightSum', 'demand', 'existing']    
            )

            
    def forElements(self):
        return self.__forElements

    def getValues(self):
        return self.__values