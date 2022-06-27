from SingletonMeta import SingletonMeta

class Singleton(metaclass=SingletonMeta):

    def BusinessLogic(self)->str:
        return "Business Logic"
