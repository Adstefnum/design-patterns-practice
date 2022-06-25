from Builders.WoodenHouseBuilder import WoodenHouseBuilder
from Builders.WoodenHouseWithPoolBuilder import WoodenHouseWithPoolBuilder
from Builders.TimeCrystalHouseBuilder import TimeCrystalHouseBuilder

class Director:

    def __init__(self):
        self.builder = builder

    def buildWoodenHouse(self)->WoodenHouseBuilder:
        return WoodenHouseBuilder()

    def buildWoodenHouseWithPool(self)->WoodenHouseWithPoolBuilder:
        return WoodenHouseWithPoolBuilder()

    def buildTimeCrystalHouse(self)->TimeCrystalHouseBuilder:
        return TimeCrystalHouseBuilder()
