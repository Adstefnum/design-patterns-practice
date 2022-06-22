from __future__ import annotations
from abc import ABC, abstractmethod

class TransportInterface(ABC):

  @abstractmethod
  def generalBusinessLogic(self)->str:
    pass