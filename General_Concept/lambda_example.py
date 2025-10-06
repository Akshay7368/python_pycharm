a = lambda :'----------------'
#print(a())
a2 = lambda a: a ** 2
#print(a2(5))


a3 = lambda a, b: a ** 2 + b ** 2 + 2 * a * b
# print(a3(3, 5))
# print(a3(3,3))

a4 = lambda a=2, b=3, c=6: a+b+c / 2
# print(int(a4(1,2,3)))
# print(int(a4()))
# print(int(a4(9,6)))

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)
