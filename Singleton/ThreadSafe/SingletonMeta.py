from threading import Lock

class SingletonMeta(type):

    _instances = {}
    lock:Lock = Lock()

    def __call__(cls,*args,**kwargs):
        #the first thread to reach here creates the instance and locks it for subsequent thread so they use a single instance
        with cls.lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]
