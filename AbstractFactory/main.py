from AbstractFactoryInterface import AbstractFactory
from ModernEraFactory import ModernEraFactory
from VictorianEraFactory import VictorianEraFactory

def client(factory:AbstractFactory)->None:
  chair = factory.CreateChair()
  coffeeTable  = factory.CreateCoffeeTable()
  sofa = factory.CreateSofa()

  print("---Chair---")
  print(chair.HasLegs())
  print(chair.CaclculateMaxWeightCanCarry())
  print("\n")

  print("---CoffeeTable---")
  print(coffeeTable.HasFourLegs())
  print(coffeeTable.CaclculateMaxSensibleHeight())
  print("\n")

  print("---Sofa---")
  print(sofa.HasFourShortLegs())
  print(sofa.HasSoftSurface())
  print("\n")


if __name__ == "__main__":
  print("******Modern Era******")
  client(ModernEraFactory())

  print("******Victorian Era******")
  client(VictorianEraFactory())