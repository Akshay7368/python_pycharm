# Poly means many so many forms
# inbuilt polymorphism
from numpy.ma.core import squeeze

a= 10
b= 15
print(a+b)
a="Hello"
b="world"
print(a+b)
a='2'
b=4
print(a*b)


# Function with polymorphism
# Interview Question
def sum_of_numbers(*args):
    sum = 0
    for a in args:
        sum+=a
    return sum


x = sum_of_numbers(2,1,4,6)
x1= sum_of_numbers(354,67)
x3=sum_of_numbers(13,6,8,4,3,6,3,7,9,4,2,25,0)
print(x)
print(x1)
print(x3)


# class with polymorphism

class India:
    def geographical_location(self):
        print("It belongs to Asian Continent")

    def population_count(self):
        print("145_Crores")

    def country_type(self):
        print("Developed Country")


class USA:
    def geographical_location(self):
        print("It belongs to North America Continent")

    def population_count(self):
        print("100_Crores")

    def country_type(self):
        print("Developed Country")


class Russia:
    def geographical_location(self):
        print("It belongs to Asian Continent")

    def population_count(self):
        print("50 Crores")

    def country_type(self):
        print("Developed Country")


I = India()
U = USA()
R = Russia()
for o in (I, U, R):
    o.geographical_location()
    o.population_count()
    o.country_type()
    print("*" * 25)



# Inheritance with polymorphism
class shape:
    def __init__(self):
        print("*" * 20)

class circle():
    def __init__(self,radius):
        self.radius = radius
    def volume(self):
        print(f"Volume of circle of {self.radius} = {3.14 * (self.radius)}")


class Square():
    def __init__(self,side):
        self.side = side
    def volume(self):
        print(f"Volume of Square of {self.side} = {self.side ** 2}")


c= circle(5)
s= Square(4)

for v in (c,s):
    v.volume()
















