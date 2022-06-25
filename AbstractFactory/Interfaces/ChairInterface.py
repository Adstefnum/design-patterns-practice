from __future__ import annotations
from abc import ABC, abstractmethod

class ChairInterface(ABC):

  @abstractmethod
  def HasLegs(self)->bool:
    pass

  @abstractmethod
  def CaclculateMaxWeightCanCarry(self)->float:
    pass
