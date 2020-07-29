from scgen.main.Generator import Generator

from scgen.elements.Suppliers import Suppliers
from scgen.elements.Plants import Plants
from scgen.elements.Materials import Materials
from scgen.elements.TimePeriods import TimePeriods
from scgen.elements.Scenarios import Scenarios

from scgen.modules.Demand import Demand
from scgen.modules.Allocation import Allocation
from scgen.modules.ShippingTimes import ShippingTimes
from scgen.modules.PurchasePrice import PurchasePrice
from scgen.modules.ShippingCost import ShippingCost
from scgen.modules.Inventory import Inventory
from scgen.modules.ShippingLane import ShippingLane
from scgen.modules.Capacity import Capacity
from scgen.modules.Arc import Arc
from scgen.modules.Disruption import Disruption
from scgen.modules.MitigationCapacity import MitigationCapacity
from scgen.modules.NumberSuppliersLimit import NumberSuppliersLimit
from scgen.modules.SupplierActivationCost import SupplierActivationCost

from scgen.distributions.Uniform import Uniform
from scgen.distributions.UniformIntegral import UniformIntegral
from scgen.distributions.Bernoulli import Bernoulli
from scgen.distributions.Constant import Constant

availableElements = [
    Suppliers,
    Plants,
    Materials,
    TimePeriods,
    Scenarios
]

availableModules = [
    Demand, 
    Allocation,
    ShippingTimes,
    PurchasePrice,
    ShippingCost,
    Inventory,
    ShippingLane,
    Capacity,
    Arc,
    Disruption,
    MitigationCapacity,
    NumberSuppliersLimit,
    SupplierActivationCost
]

availableDistributions = [
    Uniform,
    UniformIntegral,
    Bernoulli,
    Constant
]

class DefaultGeneratorFactory:
    @staticmethod
    def getDefaultGenerator():
        generator = Generator()

        for element in availableElements:
            generator.registerElement(element)

        for module in availableModules:
            generator.registerModule(module)

        for distribution in availableDistributions:
            generator.registerDistribution(distribution)

        return generator
