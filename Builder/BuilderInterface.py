from __future__ import annotations
from abc import ABC,abstractmethod

class Builder(ABC):

  @abstractmethod
  def buildFoundation(self)->None:
    pass

  @abstractmethod
  def buildWalls(self)->None:
    pass

  @abstractmethod
  def buildRooms(self)->None:
    pass

  @abstractmethod
  def buildDoors(self)->None:
    pass

  @abstractmethod
  def buildWindows(self)->None:
    pass

  @abstractmethod
  def buildRoof(self)->None:
    pass

  @abstractmethod
  def buildSwimmingPool(self)->None:
    pass

  @property
  @abstractmethod
  def product(self)->None:
    pass

