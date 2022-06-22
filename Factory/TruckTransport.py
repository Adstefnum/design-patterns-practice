from TransportFactory import TransportFactory
from TransportInterface import TransportInterface

class TruckTransportFactory(TransportFactory):

  def createTransport(self)->TransportInterface:
    return TruckTransport()

class TruckTransport(TransportInterface):

  def generalBusinessLogic(self)->str:
    return "Result of Truck Transport"