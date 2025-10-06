'''
def hello():
    print("Hello world")
hello()

def hello2():
    return "hello world"
ans = hello2()
print(ans)
'''

def tempchk(t):
    if t < 0 :
        return "cold"
    elif t > 0 and t <=10:
        return "0 - 10 degree"
    elif t >=11 and t <= 25:
        return "11 - 25 degree"
    else:
        return "Above 25 degree"
ans = tempchk(1)
# print(ans)

t1= [12,-2,54,23,41,-14,15,32,24,-21,-11,-1,6]
lst = []
for i in range(len(t1)):
    lst.append(tempchk(t1[i]))
# print(t1)
# print(lst)
final = list(zip(t1,lst))
# print(final)

def loginchk(username, password):
    if username != 'admin' and password != 'admin':
        return "Incorrect username and password"
    elif username == 'admin' and password != 'admin':
        return "Incorrect details"
    elif username != 'admin' and password == 'admin':
        return "Incorrect details"
    else:
        return "Successfull login"
# ans = loginchk('admin', 'sds')
# print(ans)
