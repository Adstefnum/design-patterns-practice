from __future__ import annotations
from abc import ABC, abstractmethod

class CoffeeTableInterface(ABC):

  @abstractmethod
  def HasFourLegs(self)->bool:
    pass

  @abstractmethod
  def CaclculateMaxSensibleHeight(self)->float:
    pass
