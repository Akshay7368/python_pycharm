

# a = [2,5,7,9,1,12,4,10]
# b = [4,9,12,3,43,1,11]
# out = list(zip(a, b))
# print(out)
# out1 = set(zip(a,b))
# print(out1)
# out2 = tuple(zip(a , b))
# print(out2)
# out3 = dict(zip(a, b))
# print(out3)


from lambda_example import *
Weekday = [1,2,3,4,5,6,7]
weekdayname = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
working_type = ['Leave', 'workingday', 'workingday', 'workingday', 'workingday', 'workingday', 'Leave']
Ans = list(zip(Weekday,weekdayname,working_type))
print(Ans)
print(a())
c, d, e = zip(*Ans)
print(c)
print(a())
print(d)
print(a())
print(e)
print(a())

lst1 = [1,2,3,4,5]



