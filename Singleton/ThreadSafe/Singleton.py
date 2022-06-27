from SingletonMeta import SingletonMeta

class Singleton(metaclass=SingletonMeta):
    value:str

    def __init__(self,value):
        self.value = value

    def BusinessLogic(self)->str:
        return "Business Logic"
