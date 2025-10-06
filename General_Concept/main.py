from calculation import add, sub, mul, div
print("Lambda calculator")
print("Enter any operations +, -, *, /")
operation = input("Enter the operation: ")
first_num = int(input("Enter the 1st num:"))
sec_num = int(input("Enter the 2nd num: "))

if operation == '+':
    print("Result:", add(first_num, sec_num))
elif operation == '-':
    print("Result:", sub(first_num, sec_num))
elif operation == '*':
    print("Result:", mul(first_num, sec_num))
elif operation == '/':
    print("Result:", div(first_num, sec_num))
else:
    print("Invalid operation")