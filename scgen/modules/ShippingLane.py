from scgen.base_components.Module import Module
from scgen.helpers.JointGeneration import generateJointly

import pandas as pd

class ShippingLane(Module):
    name = "shippingLane"

    def __init__(self, forElements, distributionTransportTime, distributionSafetyStock, elementList, moduleList, distributionsProvider, **additionalSettings):
        self.__forElements = forElements

        self.checkForRequirement("arc", moduleList)

        transportTime = generateJointly(
            forElements = forElements,
            distributionSettings = distributionTransportTime,
            elementList = elementList,
            distributionsProvider = distributionsProvider
        ).rename(columns = {"_value": "transportTime"})

        safetyStock = generateJointly(
            forElements = forElements,
            distributionSettings = distributionSafetyStock,
            elementList = elementList,
            distributionsProvider = distributionsProvider
        ).rename(columns = {"_value": "safetyStock"})

        arc = moduleList["arc"].getValues()

        transportValuesOnArcs = (
            transportTime
            .merge(safetyStock)
            .merge(arc) 
        )

        # only include rows that correspond to existing arcs
        filteredTransportValues = (
            transportValuesOnArcs[transportValuesOnArcs.existing == 1]
            .drop(columns = ["existing"])
        )

        self.__values = filteredTransportValues   
            
    def forElements(self):
        return self.__forElements

    def getValues(self):
        return self.__values