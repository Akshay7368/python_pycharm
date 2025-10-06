class grand_father():
    def __init__(self,g_name,g_age,g_location):
        self.g_name = g_name
        self.g_age = g_age
        self.g_location = g_location

    def grand_father_print(self):
        print(f"Name of the grandfather is {self.g_name} and age is {self.g_age} from {self.g_location}")


class father(grand_father):
    def __init__(self,g_name,g_age,g_location,f_name,f_age,f_location):
        grand_father.__init__(self,g_name,g_age,g_location)
        self.f_name = f_name
        self.f_age = f_age
        self.f_location = f_location

    def father_print(self):
        print(f"Name of the grandfather is {self.f_name} and age is {self.f_age} from {self.f_location}")


class son(father):
    def __init__(self,g_name,g_age,g_location,f_name,f_age,f_location,s_name,s_age,s_location):
        father.__init__(self,g_name,g_age,g_location,f_name,f_age,f_location)
        self.s_name = s_name
        self.s_age = s_age
        self.s_location = s_location

    def son_print(self):
        print(f"Name of the grandfather is {self.s_name} and age is {self.s_age} from {self.s_location}")


x = son('Raja',90,'Madurai','Ravi',50,'Kovai','Ram',20,'Chennai')
x.grand_father_print()
x.father_print()
x.son_print()