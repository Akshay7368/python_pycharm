from lambda_example import *
from F1 import *
lst = [2,4,5,7,8,9]
ans = list(map(a2, lst))
print(ans)
print(a())
x = [12,3,4,5,7]
y = [2,8,9,4,21]
ans1 = list(map(a3, x, y))
print(ans1)
print(a())
print(list(zip(x, y, ans1)))

username_lst = ['Admin123', 'admin', 'akshay1', 'kumar123']
pass_lst = ['ak123', 'admin', 'new1', 'besant1']
output = list(map(loginchk, username_lst, pass_lst))
print(a())
print(output)
print(a())
print(list(zip(username_lst,pass_lst,output)))

