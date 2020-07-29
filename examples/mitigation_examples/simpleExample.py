import sys

sys.path.append('../')

from scgen.main.DefaultGeneratorFactory import DefaultGeneratorFactory

gen = DefaultGeneratorFactory.getDefaultGenerator()

exampleSettings = {
    "elements": [
        {
            "type": "suppliers",
            "count": 4
        },
        {
            "type": "plants",
            "count": 3
        },
        {
            "type": "materials",    
            "count": 2
        },
        {
            "type": "timePeriods",
            "count": 12
        }
    ],
    "modules": [
        {
            "type": "demand",
            "forElements": ["plants", "materials", "timePeriods"],
            "distributions": [
                {
                    "dependingOnElements": ["plants"],
                    "type": "uniform",
                    "min": 0.5,
                    "max": 0.5
                },
                {
                    "dependingOnElements": ["materials"],
                    "type": "uniform",
                    "min": 0.0,
                    "max": 1.0
                },
                { 
                    "dependingOnElements": ["materials", "timePeriods"],
                    "type": "uniform",
                    "min": 0.8,
                    "max": 1.2
                }
            ]
        }    
    ]
}

gen.generate(exampleSettings)

print(gen.getOutput())