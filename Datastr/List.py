'''
Num = [2, 4, 5, 6, 8]
print(Num[1:])
# print(Num[2], Num[-1])
# print(max(Num), min(Num), len(Num), sum(Num))
# # print(dir(Num))

# Num1 = []
# Num1.append(5)
# Num1.append(9)
# Num1.insert(1, 4)
# Num1.extend(Num)
# Num1.pop()
# print(Num1)

# A = [3,5,7,3,1,1,3,2,5,7,9,33,556,2,12,]
# # A.sort()
# # A.sort(reverse=True)
# # print(A)
# # B = A
# # print(B)
# # B.clear()
# # print(B)
#
# print(A.count(2))
# print(len(A))
# print(A.index(4))
# print(A[3])

# A =[2,3,4,5,7,7,8,15,12,11]
# A.append(99)
# A.insert(5,20)
# A.sort(reverse=True)
#
# print(A)

# List1 =[23, 54,76,344,27,2,4,2, 65]
# List2 =[12, 32, 45, 43, 2, 75]
# print(max(List1), min(List1),len(List1),sum(List1))
# print("---------")
# List1.append(99)
# # List1.extend(List2)
# # print(List1)
# print("---------")
# List1.insert(2, 5)
# List2.insert(0, 1)
# print(List1,List2)
# L = List1.copy()
# print(L)
# L.clear()
# print(L)
# print(List1, List2)
# List1.pop(2)
# print(List1)
# List2.remove(2)
--------------------------------------------------------
#list comprehension

ans = [i**2 for i in range(11)]
print(ans)

even = [i for i in range(1, 51) if i %2==0]
print(even)

#workout examples from udemy..................

list = []
for i in range(1, 21):
    list.append(i)
print(list)
print(len(list))
print(list[0], list[len(list) // 2], list[-1])
print(list[::-1])
list.sort(reverse=True)
print(list)
''''''

import random
list= []
for i in range(11):
    numm = random.sample(range(1, 100), 1)
    list.append(numm)
print(list)
'''

'''Num = [1,2,3,4,5,6,7,8,9,10]
A, *B, C = Num
print(A)
print(B)
print(C)
Num[1], Num[3] = Num[3], Num[1]
print(Num)



list=[]
print(type(list))

set =dict()

print(type(set))
'''

inventory = ["Apples", "mangoes", "berry", "Guava"]
inventory.append("Watermelon")
inventory.remove("Guava")
item = input("Enter any item to check: ")
if item in inventory:
    print(f"{item} are in stock. ")
else:
    print(f"{item} are out of stock. ")
print("inventory List: ")
for item in inventory:
    print(f"- {item}")