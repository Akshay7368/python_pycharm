import csv
with open('student1.csv', mode='r', newline='') as file:
    r = csv.reader(file)
    for row in r:
        print(row)
