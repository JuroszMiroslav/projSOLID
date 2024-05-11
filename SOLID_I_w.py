from abc import ABC, abstractmethod

# Define an abstract base class (ABC) for Bird with two abstract methods
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def walk(self):
        pass

# Ostriche is a type of Bird but cannot fly,
# so an exception is raised when fly method is called
class Ostriche(Bird):
    def fly(self):
        # Not an appropriate design,
        # violates Interface Segregation Principle (ISP)
        raise Exception("Ostriche is not flying")

    def walk(self):
        print("Ostriche is walking")

# Eagle is a type of Bird that can both fly and walk
class Eagle(Bird):
    def fly(self):
        print("Eagle is flying")

    def walk(self):
        print("Eagle is walking")

# Create instances and call methods
try:
    obj = Eagle()
    obj.fly()
    obj.walk()
    obj2 = Ostriche()
    obj2.walk()
    # Will raise an exception as ostriches can't fly
    obj2.fly()
except Exception as e:
    # Print the exception message
    print(e)