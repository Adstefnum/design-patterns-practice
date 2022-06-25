from Interfaces.ChairInterface import ChairInterface

class ModernEraChair(ChairInterface):

  def HasLegs(self)->bool:
    return True


  def CaclculateMaxWeightCanCarry(self)->float:
    return 10.0

