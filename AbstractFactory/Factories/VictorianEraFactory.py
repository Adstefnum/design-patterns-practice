from Factories.AbstractFactoryInterface import AbstractFactory
from Products.VictorianEraChair import VictorianEraChair
from Products.VictorianEraSofa import VictorianEraSofa
from Products.VictorianEraCoffeeTable import VictorianEraCoffeeTable
from Interfaces.ChairInterface import ChairInterface
from Interfaces.SofaInterface import SofaInterface
from Interfaces.CoffeeTableInterface import CoffeeTableInterface

class VictorianEraFactory(AbstractFactory):
  def CreateChair(self)->ChairInterface:
    return VictorianEraChair()

  def CreateSofa(self)->SofaInterface:
    return VictorianEraSofa()

  def CreateCoffeeTable(self)->CoffeeTableInterface:
    return VictorianEraCoffeeTable()

