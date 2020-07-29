import sys
import json

from scgen.main.DefaultGeneratorFactory import DefaultGeneratorFactory

if __name__ == "__main__":
    givenInput = sys.stdin.read()
    
    settings = json.loads(givenInput)

    gen = DefaultGeneratorFactory.getDefaultGenerator()

    gen.generate(settings)

    print(gen.output().getJson())