from Target import Target
from Adaptee import Adaptee
from Adapter import Adapter

def client(target)->None:
    print(target.request())

if __name__ == '__main__':
    print("\n-----Target-----")
    target = Target()
    client(target)

    print("\n-----Adaptee-----")
    adaptee = Adaptee()
    print(adaptee.specific_request())

    print("\n-----Adapter-----")
    adapter = Adapter()
    print("\nreversing the string")
    client(adapter)
