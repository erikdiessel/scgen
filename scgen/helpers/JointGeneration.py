from itertools import product, combinations
from functools import reduce

from scgen.helpers.dataframes import createDataFrameWithKeys

import pandas as pd

def subsets(s):
    for cardinality in range(len(s) + 1):
        yield from combinations(s, cardinality)

def generateJointly(forElements, elementList, distributionSettings, distributionsProvider):
    """

    distributions: 
    """    

    elementSubsets = list(subsets(sorted(forElements)))
    factors = {
        elementSubset: createDataFrameWithKeys(elementSubset, elementList)
        for elementSubset in elementSubsets
        if elementSubset != ()
    }

    # initialize factors with default value 1:
    for df in factors.values():
        df['_value'] = 1.0

    baselineValue = 1.0

    # Overwrite some of the factors, if given by a distribution
    for setting in distributionSettings:
        distributionType = distributionsProvider[setting["type"]]
        instantiatedDistribution = distributionType(**setting)
        distributionForElements = tuple(sorted(setting["dependingOnElements"]))
        # the case of setting a baseline value is treated differently
        if distributionForElements == ():
            baselineValue = instantiatedDistribution.generate()
        else:
            # Make sure that this key makes sense in the factors
            assert distributionForElements in elementSubsets

#             factors[distributionForElements] = factors[distributionForElements].assign(
#                 _value = lambda _: instantiatedDistribution.generate()
#             )
            factors[distributionForElements]['_value'] = [
                instantiatedDistribution.generate()
                for _ in range(len(factors[distributionForElements]))
            ]

    values = createDataFrameWithKeys(forElements, elementList)

    mergedDfs = [
        pd.merge(values, factor)
        for factor in factors.values()
    ]

    factorProduct = reduce(
        lambda df1, df2: df1.merge(
            df2, 
            on = forElements,
            suffixes = ['_1', '_2']
        ).assign(
            _value = lambda df: df['_value_1'] * df['_value_2']
        ).drop(
            columns = ['_value_1', '_value_2']
        ),
        mergedDfs
    )

    factorProduct['_value'] *= baselineValue 

    return factorProduct

    # values['_value'] = baselineValue * factorProduct

    # return values
