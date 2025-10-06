import csv
n = int(input("Enter the number of students: "))
st=[]
for i in range(1, n+1):
    temp=[]
    ID = input("Enter the id:")
    name = input("Enter the name:")
    m1 = int(input("enter the mark1:"))
    m2 = int(input("enter the mark2"))
    m3 = int(input("enter the mark3:"))
    total = m1 + m2 + m3
    avg = total / 3
    temp.append(ID)
    temp.append(name)
    temp.append(m1)
    temp.append(m2)
    temp.append(m3)
    temp.append(total)
    temp.append(avg)
    st.append(temp)
    print(temp)
    print(st)
with open('student1.csv', mode='a', newline='') as file:
    wr = csv.writer(file)
    wr.writerows(st)