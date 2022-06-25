from Interfaces.SofaInterface import SofaInterface

class VictorianEraSofa(SofaInterface):

  def HasFourShortLegs(self)->bool:
    return True

  def HasSoftSurface(self)->bool:
    return True

