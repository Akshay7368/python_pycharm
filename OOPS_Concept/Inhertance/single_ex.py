# Points to remember
# We should create object only for Child Class

class father:
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location

    def father_print(self):
        print(f"Name of the father is {self.name} and age is {self.age} from {self.location}")


class Son(father):
    def __init__(self,name,age,location,s_name,s_age,s_location):
        father.__init__(self,name,age,location)
        self.s_name = s_name
        self.s_age = s_age
        self.s_location = s_location

    def son_print(self):
        print(f"Name of the Son is {self.s_name} and age is {self.s_age} from {self.s_location}")


y = Son('Akshay',23,'Chennai','Kumar',12,'Chennai')
y.father_print()
y.son_print()










