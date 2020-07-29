from scgen.base_components.Module import Module
from scgen.helpers.JointGeneration import generateJointly

import pandas as pd
from random import choice
import numpy as np

from scgen.helpers.dataframes import createDataFrameWithKeys


class Arc(Module):
    name = "arc"

    def __init__(self, fromElements, toElements, distributions, elementList, moduleList, distributionsProvider, **additionalSettings):
        self.__forElements = fromElements + toElements

        toElementsCombinations = createDataFrameWithKeys(
            toElements,
            elementList
        )
        # Make sure that the solution is feasible
        # by having at least one arc
        # for every combination of the *toElements*
        skeletonArcs = toElementsCombinations.assign(**{
            element: [choice(elementList[element].members()) for _ in range(len(toElementsCombinations))]
            for element in fromElements
        }).assign(
            existing = 1
        )

        forElements = fromElements + toElements

        if distributions == "default":
            # At default, choose all arcs to be existing
            indicators = (
                createDataFrameWithKeys(forElements, elementList)
                .assign(existing = 1)
            )
        else: 
            indicators = generateJointly(
                forElements = forElements,
                distributionSettings = distributions,
                elementList = elementList,
                distributionsProvider = distributionsProvider
            ).rename(columns = {"_value": "existing"})

        # set an arc to existing status
        # if it is existing in the skeleton arcs or
        # the random indicators
        arcs = pd.concat(
            [ skeletonArcs, indicators ],
            sort = True
        ).groupby(
            forElements,
            as_index = False
        ).max()


        self.__values = arcs
        

            
    def forElements(self):
        return self.__forElements

    def getValues(self):
        return self.__values