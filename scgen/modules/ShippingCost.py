import pandas as pd
from scgen.base_components.Module import Module

from scgen.helpers.JointGeneration import generateJointly


class ShippingCost(Module):
    name = "shippingCost"

    def __init__(self, forElements, distributions, elementList, moduleList, distributionsProvider, **additionalSettings):
        self.__forElements = forElements

        if not "demand" in moduleList:
            raise ValueError("The module allocation requires a demand module initialized before")

        # shipping cost door to port
        dtp = generateJointly(
            forElements = forElements,
            distributionSettings = distributions,
            elementList = elementList,
            distributionsProvider = distributionsProvider
        ).rename(columns = {"_value": "shippingCost_dtp"})

        # shipping cost port to door
        ptd = generateJointly(
            forElements = forElements,
            distributionSettings = distributions,
            elementList = elementList,
            distributionsProvider = distributionsProvider
        ).rename(columns = {"_value": "shippingCost_ptd"})

        self.__values = pd.merge(
            dtp,
            ptd
        ).assign(
            shippingCost = 
            lambda df: df["shippingCost_dtp"] + df["shippingCost_ptd"]
        )
            
    def forElements(self):
        return self.__forElements

    def getValues(self):
        return self.__values