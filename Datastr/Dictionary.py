# D1 = {'Id': 1, 'Name': "Akshay"}
# print(D1)
# # print(dir(D1))


# Aadhar = {'An': '124-3232-322', 'name': "Akshay", 'add': '123 chennai', 'phn': 33244343, 'phn': 434324324}
# print(Aadhar)
# # New = Aadhar.copy()
# # print(New)
# # New.clear()
# # print(New)
#
# print(Aadhar.keys())
# print(Aadhar.values())
# print(Aadhar.items())

# K = {'A', 'E', 'I', 'O', 'U'}
#
# Ans = dict.fromkeys(K,0)
# print(Ans)
# #
# My_dict = {'ID':1, 'Name': "Akshay", 'location': 'Mumbai'}
# My_dict.setdefault('location', 'chennai')
# print(My_dict)
'''
emp_dict = {"Akshay": 23, "Surya": 12, "Vijay": 25, "Dhanush": 33, "Peter": 8, "Arjun": 30}
for k, v in emp_dict.items():
    if v >= 18:
        print(f"{k} is allowed to vote")
    else:
        print(f"{k} is not eligible to vote")

student= {

    "name": "Akshay",
    "age": 24,
    "course": "Data Science"
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("age"))
student["name"] = "Kumar"
student["Location"] = "Chennai"
print(student)

for key, values in student.items():
    print(key)
    print(values)


students = {
    "student1" : {"name": "Akshay", "age": 23},
    "student2" : {"name": "Kumar", "age": 25}
}
print(students["student2"]["name"])


##Dictionary Comprehensiom

Squares={x: x**2 for x in range(5)}
print(Squares)

even = {x: x**2 for x in range(11) if x % 2 == 0}
print(even)

numbers = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number]+= 1
    else:
        frequency[number] = 1
print(frequency)

'''

A = {"Name": "Akshay", "Age": 23}
B = {"Gnder": "M", "Location": "Chenai"}
merge = {**A, **B}
print(merge)






