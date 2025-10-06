'''tuple= ()
t1= (1,3,4,5,6,9)
print(dir(t1))

t2 =(1,2,3,5,5,3,2,10,12,2,2,2)
# print(t2.count(2))
# print(t2.index(5))
# print(max(t2),min(t2),len(t2),sum(t2))
print(t2[4])
print(t2[:])'''

'''tpl = (1, "Hi", 3.11, True)
print(tpl)
tpl[1]= "Bye"
print(tpl)'''

numbers = [1, 2, 3, 4, 5]
first, *middle,last = numbers
print(first)
print(middle)
print(last)