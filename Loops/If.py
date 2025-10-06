'''
if 'w':  #(we can give any name are numbers after it will run either false or 0)
    print("Welcome")
'''

'''
age = int(input("Enter the age: "))
if age >= 18:
    print("Vote")
else:
    print(f"You have to wait for {18 - age} years to vote")
    
----------------------------------------------------------------

n = int(input("Enter the number: "))
if n<0:
    print("You have entered a negative number")
elif n==0:
    print("You have entered Zero")
elif n>0 and n<=10:
    print("Number is between 1 to 10")
else:
    print("Number is greater than 10")



Id = int(input("Enter the id: "))
name = input("Enter the name: ")
M1 = int(input("Enter the 1st mark: "))
M2 = int(input("Enter the 2nd mark: "))
M3 = int(input("Enter the 3rd mark: "))
if M1 < 35 or M2 < 35 or M3 < 35:
    if M1 < 35 and M2 < 35 and M3 < 35:
        print("failed in all 3 subjects")
    elif M1 < 35 and M2 < 35:
        print("failed in 1 and 2 subjects")
    elif M1 < 35 and M3 < 35:
        print("Failed in 1 and 3 subjects")
    elif M2 < 35 and M3 < 35:
        print("Failed in 2 and 3 subjects")
    elif M1 < 35:
        print("Failed in 1")
    elif M2 < 35:
        print("Failed in 2")
    else:
        print("Failed in 3")
else:
    print("You have passed in all 3 subjects")
    total = M1 + M2 + M3
    Average = total / 3
    print(f"""
          student_id = {Id}
          student_name = {name}
          mark1 ={M1}
          mark2 = {M2}
          mark3 = {M3}
          total = {total}
          avg = {Average}
    """)


#username and password check
user_name = "Admin"
Pass = "Password"

A = input("Enter the user_name: ")
B = input("Enter the password: ")

if user_name == A:
    if Pass == B:
        print("Login Successfull")
    else:
        print("Wrong password")
else:
    print("username not valid")
    


num = int(input("enter a number: "))

if (num % 5 == 0) or (num % 11 == 0):
    print(f"{num} is divisible by 5 or 11 ")
else:
    print("Not divisible")
    
'''

year = int(input("enter the year: "))

if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")