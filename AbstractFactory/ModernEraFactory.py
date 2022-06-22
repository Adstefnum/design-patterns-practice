from AbstractFactoryInterface import AbstractFactory
from ModernEraChair import ModernEraChair
from ModernEraSofa import ModernEraSofa
from ModernEraCoffeeTable import ModernEraCoffeeTable
from ChairInterface import ChairInterface
from SofaInterface import SofaInterface
from CoffeeTableInterface import CoffeeTableInterface

class ModernEraFactory(AbstractFactory):  
  def CreateChair(self)->ChairInterface:
    return ModernEraChair()

  def CreateSofa(self)->SofaInterface:
    return ModernEraSofa()

  def CreateCoffeeTable(self)->CoffeeTableInterface:
    return ModernEraCoffeeTable()
  