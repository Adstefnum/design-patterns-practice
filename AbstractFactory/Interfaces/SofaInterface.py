from __future__ import annotations
from abc import ABC, abstractmethod

class SofaInterface(ABC):

  @abstractmethod
  def HasFourShortLegs(self)->bool:
    pass

  @abstractmethod
  def HasSoftSurface(self)->bool:
    pass
