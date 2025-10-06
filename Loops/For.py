'''
for a in range(5):
    print(a)

for a in range(1, 10, 5):

    print(a)

for a in range(1, ):
    age = int(input("Enter the age: "))
    if age >= 18:
        print("Vote")
    else:
        print(f"You have to wait for {18 - age} years to vote")


List = []
for a in range(1, 11):
    List.append(a * 3)
print(List)


#print all even numbers between 1 to 50

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


#Print the sum of all numbers from 1 to 100

sum = 0
for i in range(1,101):
    sum+= i
print(sum)

#multiplication table

num = int(input("Enter the no: "))
print(f"multiplication table for {num} is : ")
for i in range(1,11):
    print(f" {num} x {i} = {num * i}")

#print the vowels
a = input("Enter the char :")
for char in a:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(char)



#print each character in the string

str = "Akshay Kumar"
for char in str:
    print(char)


#factorial of a number

n = int(input("Enter the num: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    print(fact)



#print square numbers from 1 - 10

for i in range(1, 11):
    num = i * i
    print(num, end=" ")

n = 5
for i in range(n):
    for j in range(i + 1):
        print(f"{i}", end=" ")

    print()


# In class...
row = int(input("Enter the no of rows: "))
columns = int(input("Enter the no of columns: "))
for i in range(1, row+1):  # print the rows
    for j in range(1, columns+1):   # print the columns
        print(f"{i} * {j} = {i * j}", end= " ")
    print() # This print will enter's the next line


for a in range(6):
    for b in range(1, a + 1):
        print("*" , end= " ")
    print()



c = 1
for a in range(1, 6):
    for b in range(1, a + 1):
        print(c, end=" ")
        c += 1
    print()


for a in range(65, 92):
    print(a, chr(a))


c= 65
for a in range(1, 10):
    for b in range(1, a + 1):
        print(chr(c), end=" ")
    c+= 1
    print()


for a in range(1, 10):
    if a == 5:
        for b in range(1, 5):
            print("*", end= " ")
        print()
    else:
        for b in range(1, 5):
            if b == 1 or b == 4:
                print("*", end=" ")
            else:
                print(" ", end= " ")
        print()




# output will be as P
for a in range(1, 10):
    if a == 1 or a == 5:
        for b in range(1, 5):
            print("*", end=" ")
        print()
    elif a == 2 or a == 3 or a == 4:
        for b in range(1, 5):
            if b == 1 or b == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    else:
        for b in range(1, 5):
            if b == 1:
                print("*", end=" ")
            else:
                print(" ", end= " ")
        print()


# output will be as A

for a in range(1, 10):
    if a == 1 or a == 5:
        for b in range(1, 5):
            print("*", end= " ")
        print()
    else:
        for b in range(1, 5):
            if b == 1 or b == 4:
                print("*", end=" ")
            else:
                print(" ", end= " ")
        print()



row = int(input("Enter the row: "))

for i in range(1, row + 1):
    for space in range(row - i):
        print(" ", end=" ")
    for star in range(2 * i - 1):
        print("*", end=" ")
    print()



for i in range(1, 6):
    for j in range(1, i+1):

        print(i * j, end=" ")
    print()
'''

























