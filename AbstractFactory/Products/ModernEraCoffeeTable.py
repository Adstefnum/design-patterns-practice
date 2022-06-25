from Interfaces.CoffeeTableInterface import CoffeeTableInterface

class ModernEraCoffeeTable(CoffeeTableInterface):

  def HasFourLegs(self)->bool:
    return True

  def CaclculateMaxSensibleHeight(self)->float:
    return 20.0

