from Interfaces.CoffeeTableInterface import CoffeeTableInterface

class VictorianEraCoffeeTable(CoffeeTableInterface):

  def HasFourLegs(self)->bool:
    return True

  def CaclculateMaxSensibleHeight(self)->float:
    return 20.0

