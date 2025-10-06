import numpy as np

'''
Total_marks = []
for a in range(1,6):
    n = int(input(f"Enter the total for student{a} = "))
    Total_marks.append(n)
print(Total_marks)
ans = np.array(Total_marks)
print(ans)
print(ans + 1)


finalst=[]
for a in range(1,6):
    sub=[]
    for b in range(1,6):
        n = int(input(f"Enter the student {a} and subject {b}marks: "))
        sub.append(n)
    finalst.append(sub)
print(finalst)
ans = np.array(finalst)
print(ans)

ans1 = np.array([[[20,45,40],[21,43,46],[12,45,67]]])
print(ans1)
print(ans1.shape)



finalst=[]
for a in range(1,4):
    sem= []
    for b in range(1,5):
        sub = []
        for c in range(1,4):
            n = int(input(f"Enter the student {a} and semester {b} and subject {c} marks"))
            sub.append(n)
        sem.append(sub)
    finalst.append(sem)
print(finalst)
ans = np.array(finalst)
print(ans)

print(np.array([[1,2,3,],[4,5,6],[7,8,9]]))
print(np.zeros((2,2)))
print(np.zeros((3,2,3)))


print(np.ones((3,4)))
print(np.array([[[1,2,2],[3,4,5],[1,2,3],[4,5,7]]]))
print(np.full((5),3))
print(np.eye(3))
print(np.diag((20,30,40,50)))

print(np.arange(10))
print(np.arange(11,30))

print(np.linspace(1,10,5))

#array calculations
x = np.array([11,12,13,14,15])
y = np.array([2,4,6,8,10])
print("Addition:", x+y)
print("Subtraction:",y-x)
print("Multilication:",x*y)
print("Division:",y/x)
print("Mean:",np.mean(y))
print("Median:",np.median(x))


#array insception
x = np.array([1,2,3,4,5])
y = np.array([[2,4,6],[8,10,12],[20,30,40]])
z = np.array([[[2,4,5],[7,8,9]],[[2,3,5],[7,6,10]],[[23,34,11],[5,12,33]]])
print(x)
print(y)
print(z)
print(np.shape(z))
print(np.size(z))
print(np.ndim(z))
print(z.dtype)


num1 = np.random.randint(5, 21, size = (3, 4))
print(num1)
print(np.random.rand(3,2))
print(np.random.choice([1,2,5],size = 5))


x = np.array([1,2,3,4,5])
y = np.array([[2,4,6],[8,10,12],[20,30,40]])
z = np.array([[[2,4,5],[7,8,9]],[[2,3,5],[7,6,10]],[[23,34,11],[5,12,33]]])
print(x[3])
print(x[-2])
print(y[0])
print(z[0][0][0])
print(np.nan)




L = [1,2,2,3,3,1,1,4,5,6,4,5,2]
print(L)
uniquevalue = np.unique(L)
print(uniquevalue)

uniquevalue1,numberofcount = np.unique(L,return_counts=True)
print(uniquevalue1)
print(numberofcount)
'''

st="""Books are our best friends. They give us knowledge, entertain us, and guide us in life. Reading every day helps us improve our language and makes us think in new ways. A good book can take us to different places, times, and even worlds, all while sitting in one place.Education is one of the most powerful tools that shapes a person’s future. It not only provides knowledge of different subjects but also helps in building character, discipline, and confidence. A well-educated person can make wise decisions, solve problems effectively, and contribute positively to society. Education also opens doors to better job opportunities and helps in improving the standard of living. Moreover, it teaches us important values such as respect, honesty, and responsibility, which are necessary for living a meaningful life. In today’s world, where technology and competition are rapidly growing, education has become more important than ever to succeed and stay ahead."""
print(st)
words=list(st.split(" "))
print(words)
uniqwords=np.unique(words)
print(uniqwords)
print(len(words))
print(len(uniqwords))
uniqword1,counts=np.unique(words,return_counts=True)
print(uniqword1)
print(counts)
print(list(zip(uniqword1,counts)))










