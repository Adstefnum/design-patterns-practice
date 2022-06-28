from Target import Target
from Adaptee import Adaptee

class Adapter(Target):
    def __init__(self,adaptee:Adaptee):
        self.adaptee = adaptee

    def request(self)->str:
        return self.adaptee.specific_request()[::-1]
