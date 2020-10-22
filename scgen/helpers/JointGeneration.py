from itertools import product, combinations
from functools import reduce

from scgen.helpers.dataframes import createDataFrameWithKeys

import pandas as pd

def subsets(s):
    for cardinality in range(len(s) + 1):
        yield from combinations(s, cardinality)

def generateJointly(forElements, elementList, distributionSettings, distributionsProvider):
    factors = []
    baselineValue = 1.0

    for setting in distributionSettings:
        distributionType = distributionsProvider[setting["type"]]
        instantiatedDistribution = distributionType(**setting)
        distributionForElements = tuple(sorted(setting["dependingOnElements"]))

        if distributionForElements == ():
            baselineValue *= instantiatedDistribution.generate()
        else:
            df = createDataFrameWithKeys(distributionForElements, elementList)
            df['_value'] = [
                instantiatedDistribution.generate()
                for _ in range(len(df))
            ]
            factors.append(df)

    values = createDataFrameWithKeys(forElements, elementList)

    mergedDfs = [
        pd.merge(values, factor)
        for factor in factors
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
