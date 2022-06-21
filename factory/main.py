from TransportFactory import TransportFactory
from ShipTransport import ShipTransportFactory
from TruckTransport import TruckTransportFactory

def main(transport:TransportFactory)->None:
  print(transport.generalBusinessLogic())

if __name__=="__main__":
  print("Using Ship Transport")
  print(main(ShipTransportFactory()))
  print("\n")

  print("Using Truck Transport")
  print(main(TruckTransportFactory()))
  print("\n")