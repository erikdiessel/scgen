import json
import pathlib
import pandas as pd


class Outputter:
    def __init__(self, elementDict, moduleDict):
        self.__elementDict = elementDict
        self.__moduleDict = moduleDict

    def createExcel(self, path):
        pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True) 
        with pd.ExcelWriter(path) as writer:
            for elementName in self.__elementDict.keys():
                df = self.__elementDict[elementName].toDataFrame()
                df.to_excel(writer, sheet_name=elementName)

            for moduleName in self.__moduleDict.keys():
                df = self.__moduleDict[moduleName].getValues()
                df.to_excel(writer, sheet_name=moduleName)

    def toDict(self):
        return {
            "elements": {
                elementName: json.loads(self.__elementDict[elementName].toDataFrame().to_json(orient="records"))
                for elementName in self.__elementDict.keys()
            },
            "modules": {
                moduleName: json.loads(self.__moduleDict[moduleName].getValues().to_json(orient="records"))
                for moduleName in self.__moduleDict.keys()
            }
        }

    def getJson(self):
        return json.dumps(self.toDict())

    def createJson(self, path):
        pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True) 

        with open(path, "w") as f:
            f.write(self.getJson())
