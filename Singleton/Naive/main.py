from Singleton import Singleton

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    if id(s1)==id(s2):
        print("Single instance used")
    else:
        print("singleton not working")
