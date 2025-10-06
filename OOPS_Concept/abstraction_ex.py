# Abstract base class

from abc import ABC, abstractmethod
from mimetypes import inited

'''class Animal(ABC):  # Abstract class

    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Sleeping...")


# Subclass must implement make_sound
class Dog(Animal):
    def make_sound(self):
        print("Bark!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# animal = Animal()  # ❌ This will raise an error: Can't instantiate abstract class
dog = Dog()
dog.make_sound()   # Output: Bark!
dog.sleep()        # Output: Sleeping...'''


class shape(ABC):
    @abstractmethod
    def volume(self):
        pass


class circle(shape):
    def __init__(self,r):
        self.r = r

    def volume(self):
        print(f"volume of circle for radius {self.r} = {3.14 * (self.r ** 2)}")


class rectangle(shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def volume(self):
        print(f"volume of rectangle of length {self.l} and breadth {self.b} = {self.l * self.b}")


class square(shape):
    def __init__(self, a):
        self.a = a

    def volume(self):
        print(f"volume od square of area {self.a} is {self.a * self.a}")


c = circle(7)
r = rectangle(3, 9)
s = square(8)

for a in (c, r, s):
    a.volume()
