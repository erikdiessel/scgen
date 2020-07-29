import pandas as pd

from itertools import product

def createDataFrameWithKeys(forElements, elementList):
    return pd.DataFrame(
        list(
            product(*(
                elementList[element].members()
                for element in forElements
            ))
        ),
        columns = forElements
    )