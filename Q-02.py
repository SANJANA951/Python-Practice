class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("The Dog Barks Bow Bow!")
    pass


d = Dog()
d.bark()
