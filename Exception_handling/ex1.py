from sys import exception

# try:
#     a = b
# except NameError as exe:
#     print(exe)
#
# a = int('abc')
# print(a)

# try:
#     a = b
# except Exception as ex:
#     print(ex)

try:
    a = 10
    b = 5
    print(b)
    c = 10
    print(b + c)
    # lst = [1,2,3,4,5]
    # print(lst[6])
except NameError:
    print("Name b is not defined")
except TypeError:
    print("We cannot add two different datatypes")
# except IndexError:
#     print("Index value is not correct")
except Exception as ex:
    print(ex)
else:
    print(a ** 2)
finally:
    print("I will always run")
