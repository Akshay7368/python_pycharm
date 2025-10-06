class School():
    def __init__(self,name,type,location):
        self.name = name
        self.type = type
        self.location = location

    def school_info(self):
        print(f"Name of the School is {self.name} and type is {self.type}, location is {self.location}")


class Student1(School):
    def __init__(self,name,type,location,s1_name, s1_age, s1_location,s1_standard):
        School.__init__(self,name,type,location)
        self.s1_name = s1_name
        self.s1_age = s1_age
        self.s1_location = s1_location
        self.s1_standard = s1_standard

    def student1_info(self):
        print(f"Name of the Student1 is {self.s1_name} and his age is {self.s1_age}, location is {self.s1_location} and his standard is {self.s1_standard}")


class Student2(School):
    def __init__(self, name,type,location,s2_name, s2_age, s2_location, s2_standard):
        School.__init__(self,name,type,location)
        self.s2_name = s2_name
        self.s2_age = s2_age
        self.s2_location = s2_location
        self.s2_standard = s2_standard

    def student2_info(self):
        print(f"Name of the Student2 is {self.s2_name} and his age is {self.s2_age}, location is {self.s2_location} and his standard is {self.s2_standard}")


x=Student1("SuperSchool","Government","Tambaram","Akshay",23,"Vandalur",12)
x=Student2("SucessSchool","Private","Avadi","kumar",25,"Chennai",11)
x.student2_info()