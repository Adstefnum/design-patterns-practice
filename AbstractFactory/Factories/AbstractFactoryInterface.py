from __future__ import annotations
from abc import ABC, abstractmethod
from Interfaces.ChairInterface import ChairInterface
from Interfaces.SofaInterface import SofaInterface
from Interfaces.CoffeeTableInterface import CoffeeTableInterface

class AbstractFactory(ABC):

  @abstractmethod
  def CreateChair(self)->ChairInterface:
    pass

  @abstractmethod
  def CreateSofa(self)->SofaInterface:
    pass

  @abstractmethod
  def CreateCoffeeTable(self)->CoffeeTableInterface:
    pass
    