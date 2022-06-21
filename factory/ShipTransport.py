from TransportFactory import TransportFactory
from TransportInterface import TransportInterface

class ShipTransportFactory(TransportFactory):

  def createTransport(self)->TransportInterface:
    return ShipTransport()

class ShipTransport(TransportInterface):

  def generalBusinessLogic(self)->str:
    return "Result of Ship Transport"
    