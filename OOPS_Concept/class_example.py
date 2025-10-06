import pyfiglet


class header:
    def __init__(self):
        figlet=pyfiglet.Figlet()
        o=figlet.renderText("Welcome to TNEB")
        print("---"*25)
        print(o)
        print("---"*25)


class footer:
    def __init__(self):
        print("*"*25)
        print('''
               Thank you!!!!😊
               Please pay bill on time otherwise service will be disconnected.
               ''')
        print("*" * 25)


class billgeneration:
    def __init__(self,unit):
        self.unit=unit

    def billcalculation(self):
        if self.unit<=100:
            bill_amount=0
        elif self.unit<=200:
            bill_amount=(100*0)+(self.unit-100)*2.35
        elif self.unit<=400:
            bill_amount=(100*0)+(100*2.35)+(self.unit-200)*4.70
        elif self.unit<=500:
            bill_amount=(100*0)+(100*2.35)+(200*4.70)+(self.unit-400)*6.30
        elif self.unit<=600:
            bill_amount=(100*0)+(300*4.70)+(100*6.30)+(self.unit-500)*8.40
        elif self.unit<=800:
            bill_amount=(100*0)+(300*4.70)+(100*6.30)+(100*8.40)+(self.unit-600)*9.45
        elif self.unit<=1000:
            bill_amount=(100*0)+(300*4.70)+(100*6.30)+(100*8.40)+(200*9.45)+(self.unit-800)*10.50
        elif self.unit>1000:
            bill_amount=(100*0)+(300*4.70)+(100*6.30)+(100*8.40)+(200*9.45)+(200*10.50)+(self.unit-1000)*11.55
        return f"Number of Units Consumed = {self.unit } and bill_amount={bill_amount}"

h=header()
a=int(input("Enter the no.units:"))
e=billgeneration(a)
o=e.billcalculation()
print(o)
a=footer()