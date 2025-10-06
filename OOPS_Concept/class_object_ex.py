#Class is a Blueprint
#We can take any number of copies as class(Objects)
#We can modify objects which will not affected original class
# __init__ It is an construtor and it is a special method
# It will run whenever the object is created
# __init__(self): default constructor
# __init__(self,a...): parameterized constructor

'''class class1:
    pass

class class2:
    print("Hello")
    print("Welcome to oops concept")

class example1:
    a=5
    b=6
    def addition(self):
        print(self.a + self.b)
x= example1()
print(x.a)
print(x.b)
x.addition()


y=example1()
print(y.a)
print(y.b)
y.addition()
y.a = 25
y.b = 45
y.addition()


z=example1()
z.a = 100
z.b = 200
z.addition()


class example3:
    a=10
    b=20
    def __init__(self):
        print("*" *40)
        print("I will run everywhere objects are created")
        print("*" * 40)

    def addition(self):
        print(self.a+self.b)
z1= example3()
z1.addition()
'''
from yaml import safe_load_all


class example4:
    def __init__(self,name,age,salary):
        print("I will assign all values to variables")
        self.name= name
        self.age = age
        self.salary = salary

    def employee_details(self):
        print(f"name = {self.name} and age = {self.age}")

    def salary_grade(self):
        if self.salary >=100000:
            print("First tier employees")
        elif self.salary >=85000:
            print("Second tier employees")
        else:
            print("Last tier employees")

o= example4('Akshay',23,50000)
o.employee_details()
o.salary_grade()

o1= example4('Kumar',26,100001)
o1.employee_details()
o1.salary_grade()
o1.salary = 87000
o1.employee_details()
o1.salary_grade()
print(o1.salary)

del o1.salary
print(o1.salary)






















