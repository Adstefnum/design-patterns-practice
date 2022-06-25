from Factories.AbstractFactoryInterface import AbstractFactory
from Products.ModernEraChair import ModernEraChair
from Products.ModernEraSofa import ModernEraSofa
from Products.ModernEraCoffeeTable import ModernEraCoffeeTable
from Interfaces.ChairInterface import ChairInterface
from Interfaces.SofaInterface import SofaInterface
from Interfaces.CoffeeTableInterface import CoffeeTableInterface

class ModernEraFactory(AbstractFactory):  
  def CreateChair(self)->ChairInterface:
    return ModernEraChair()

  def CreateSofa(self)->SofaInterface:
    return ModernEraSofa()

  def CreateCoffeeTable(self)->CoffeeTableInterface:
    return ModernEraCoffeeTable()
  