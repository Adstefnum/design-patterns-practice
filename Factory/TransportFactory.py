from __future__ import annotations
from abc import ABC, abstractmethod

class TransportFactory(ABC):

  @abstractmethod
  def createTransport(self)-> Transport:
    pass

  def generalBusinessLogic(self)->str:
    transport = self.createTransport()
    return f"I am a {transport.generalBusinessLogic()}"