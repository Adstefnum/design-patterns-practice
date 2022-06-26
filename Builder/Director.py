from BuilderInterface import Builder
from Products.TimeCrystalHouse import TimeCrystalHouse
from Products.WoodenHouse import WoodenHouse

class Director:

    def __init__(self)->None:
        self.builder = None

    @property
    def builder(self)->Builder:
        return self._builder

    @builder.setter
    def builder(self,builder:Builder)->None:
        self._builder = builder

    def buildWoodenHouse(self)->WoodenHouse:
        self.builder.buildFoundation()
        self.builder.buildWalls()
        self.builder.buildWindows()
        self.builder.buildRooms()
        self.builder.buildDoors()
        self.builder.buildWindows()

    def buildWoodenHouseWithPool(self)->WoodenHouse:
        self.builder.buildFoundation()
        self.builder.buildWalls()
        self.builder.buildWindows()
        self.builder.buildRooms()
        self.builder.buildDoors()
        self.builder.buildWindows()
        self.builder.buildSwimmingPool()

    def buildTimeCrystalHouse(self)->TimeCrystalHouse:
        self.builder.buildFoundation()
        self.builder.buildWalls()
        self.builder.buildWindows()
        self.builder.buildRooms()
        self.builder.buildDoors()
        self.builder.buildWindows()

    def buildTimeCrystalHouseWithPool(self)->TimeCrystalHouse:
        self.builder.buildFoundation()
        self.builder.buildWalls()
        self.builder.buildWindows()
        self.builder.buildRooms()
        self.builder.buildDoors()
        self.builder.buildWindows()
        self.builder.buildSwimmingPool()
