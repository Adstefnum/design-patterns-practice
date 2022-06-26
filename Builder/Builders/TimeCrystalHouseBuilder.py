from BuilderInterface import Builder
from Products.TimeCrystalHouse import TimeCrystalHouse

class TimeCrystalHouseBuilder(Builder):

  def __init__(self)->None:
        self.reset()

  def reset(self)->None:
        self._product = TimeCrystalHouse()

  @property
  def product(self)->TimeCrystalHouse:
      product = self._product
      self.reset()
      return product

  def buildFoundation(self)->None:
    self._product.add("TimeCrystal Foundation built")


  def buildWalls(self)->None:
    self._product.add("TimeCrystal Walls built")


  def buildRooms(self)->None:
    self._product.add("TimeCrystal Rooms furnished")


  def buildDoors(self)->None:
    self._product.add("TimeCrystal Victorian Doors built")


  def buildWindows(self)->None:
    self._product.add("Haha of course we used glass windows")

  def buildRoof(self)->None:
    self._product.add("TimeCrystal roof put up")

  def buildSwimmingPool(self)->None:
    self._product.add("Sweet sweet swimming pool")

