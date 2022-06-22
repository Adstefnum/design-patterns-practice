from __future__ import annotations
from abc import ABC, abstractmethod
from ChairInterface import ChairInterface
from SofaInterface import SofaInterface
from CoffeeTableInterface import CoffeeTableInterface

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
    