import csv
ID = input("Enter the id:")
name = input("Enter the name:")
m1 = int(input("enter the mark1:"))
m2 = int(input("enter the mark2"))
m3 = int(input("enter the mark3:"))
total = m1 + m2 + m3
avg = total/3

with open('student.csv', mode='a', newline='') as file:
    wr = csv.writer(file)
    wr.writerow([ID, name, m1, m2, m3, total, avg])

