from AbstractFactoryInterface import AbstractFactory
from VictorianEraChair import VictorianEraChair
from VictorianEraSofa import VictorianEraSofa
from VictorianEraCoffeeTable import VictorianEraCoffeeTable
from ChairInterface import ChairInterface
from SofaInterface import SofaInterface
from CoffeeTableInterface import CoffeeTableInterface

class VictorianEraFactory(AbstractFactory):  
  def CreateChair(self)->ChairInterface:
    return VictorianEraChair()

  def CreateSofa(self)->SofaInterface:
    return VictorianEraSofa()

  def CreateCoffeeTable(self)->CoffeeTableInterface:
    return VictorianEraCoffeeTable()
  