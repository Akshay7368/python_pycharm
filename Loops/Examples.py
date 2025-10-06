'''
import pyfiglet
n = input("Enter the name: ")
result = pyfiglet.figlet_format(n, font='chunky')
print(result)


lst = []
s = set()
d = dict()
for a in range(1, 11):
    lst.append(a ** 2)
    s.add(a ** 2)
    d[a] = a ** 2
print(lst)
print(s)
print(d)

num = [2,3,-1,4,9,14,-13,-20]
print(len(num))
for a in range(len(num)):
    if num[a] < 0:
        print(num[a], "Negative Number")
    else:
        print(num[a], "Positive numbers")

'''

emp_dict = {"Akshay": 23, "Surya": 12, "Vijay": 25, "Dhanush": 33, "Peter": 8, "Arjun": 30}
for k, v in emp_dict.items():
    if v >= 18:
        print(f"{k} is allowed to vote")
    else:
        print(f"{k} is not eligible to vote")

