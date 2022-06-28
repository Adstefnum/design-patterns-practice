from Target import Target
from Adaptee import Adaptee

class Adapter(Target,Adaptee):

    def request(self)->str:
        return self.specific_request()[::-1]
