import sys
import json

import os
script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, '..'))

from scgen.main.DefaultGeneratorFactory import DefaultGeneratorFactory

def runExample(exampleSettingsFileName, withExcel = True):
    gen = DefaultGeneratorFactory.getDefaultGenerator()

    import os
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, exampleSettingsFileName)

    with open(abs_file_path, "r") as file:
        fileContents = file.read()

    exampleSettings = json.loads(fileContents)

    gen.generate(exampleSettings)

    print(gen.output().getJson())

    if withExcel:
        excelOutputPath = os.path.join(
            script_dir, 
            "outputs/" + exampleSettingsFileName.replace(".json", ".xlsx")
        )
        gen.output().createExcel(excelOutputPath)

    jsonOutputPath = os.path.join(
        script_dir, 
        "outputs/" + exampleSettingsFileName
    )
    gen.output().createJson(jsonOutputPath)