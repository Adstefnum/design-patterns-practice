from ChairInterface import ChairInterface

class VictorianEraChair(ChairInterface):

  def HasLegs(self)->bool:
    return True
    

  def CaclculateMaxWeightCanCarry(self)->float:
    return 10.0
    