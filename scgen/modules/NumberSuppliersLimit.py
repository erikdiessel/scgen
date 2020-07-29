from scgen.modules.BaseModule import BaseModule
from scgen.helpers.JointGeneration import generateJointly

class NumberSuppliersLimit(BaseModule):
    name = "numberSuppliersLimit"

    def __init__(self, forElements, distributions, elementList, moduleList, distributionsProvider, **additionalSettings):
        super().__init__(forElements, distributions, elementList, moduleList, distributionsProvider)