class father():
    def __init__(self,fname,fage,flocation):
        self.fname = fname
        self.fage = fage
        self.flocation = flocation

    def father_print(self):
        print(f"Name of the father is {self.fname} and age is {self.fage} from {self.flocation}")


class mother():
    def __init__(self,mname,mage,mlocation):
        self.mname = mname
        self.mage = mage
        self.mlocation = mlocation

    def mother_print(self):
        print(f"Name of the Mother is {self.mname} and age is {self.mage} from {self.mlocation}")


class Son(father,mother):
    def __init__(self,fname,fage,flocation,mname,mage,mlocation,sname,sage,slocation):
        father.__init__(self,fname,fage,flocation)
        mother.__init__(self,mname,mage,mlocation)
        self.sname = sname
        self.sage = sage
        self.slocation = slocation

    def son_print(self):
        print(f"Name of the Son is {self.sname} and age is {self.sage} from {self.slocation}")


x = Son("Akshay",23,"Chennai","Swetha",23,"Chennai","Joe",2,"Chennai")
x.father_print()
x.mother_print()
x.son_print()