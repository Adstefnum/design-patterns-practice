from __future__ import annotations
from abc import ABC,abstractmethod

class BuilderFactory(ABC):

  @abstractmethod
  def buildFoundation()->str:
    pass

  @abstractmethod
  def buildWalls()->str:
    pass

  @abstractmethod
  def buildRooms()->str:
    pass

  @abstractmethod
  def buildDoors()->str:
    pass

  @abstractmethod
  def buildWindows()->str:
    pass

  @abstractmethod
  def buildRoof()->str:
    pass
    
  @abstractmethod
  def buildSwimmingPool()->str:
    pass