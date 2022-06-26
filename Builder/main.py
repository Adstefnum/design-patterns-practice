from Director import Director
from Builders.TimeCrystalHouseBuilder import TimeCrystalHouseBuilder
from Builders.WoodenHouseBuilder import WoodenHouseBuilder
from BuilderInterface import Builder

def client():
    director = Director()
    builder = TimeCrystalHouseBuilder()
    director.builder = builder

    print("------Time Crystal House-----")
    director.buildTimeCrystalHouse()
    builder.product.listParts()
    print("\n")

    print("-----Time Crystal House with Pool-----")
    director.buildTimeCrystalHouseWithPool()
    builder.product.listParts()
    print("\n")

    builder = WoodenHouseBuilder()
    director.builder = builder

    print("-----Wooden House-----")
    director.buildWoodenHouse()
    builder.product.listParts()
    print("\n")

    print("-----Wooden House with Pool-----")
    director.buildWoodenHouseWithPool()
    builder.product.listParts()
    print("\n")

if __name__ == '__main__':
    client()
