from BuilderInterface import Builder
from Products.WoodenHouse import WoodenHouse

class WoodenHouseBuilder(Builder):

  def __init__(self)->None:
        self.reset()

  def reset(self)->None:
        self._product = WoodenHouse()

  @property
  def product(self)->WoodenHouse:
      product = self._product
      self.reset()
      return product

  def buildFoundation(self)->None:
    self._product.add("Wooden Foundation built")


  def buildWalls(self)->None:
    self._product.add("Wooden Walls built")


  def buildRooms(self)->None:
    self._product.add("Wooden Rooms furnished")


  def buildDoors(self)->None:
    self._product.add("Wooden Victorian Doors built")


  def buildWindows(self)->None:
    self._product.add("Haha of course we used glass windows")

  def buildRoof(self)->None:
    self._product.add("Wooden roof put up")

  def buildSwimmingPool(self)->None:
    self._product.add("Sweet sweet swimming pool")

