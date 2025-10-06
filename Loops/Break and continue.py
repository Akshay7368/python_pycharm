

lst = [2,4,5,7,-2,7,-1]
for i in range(len(lst)):
    if lst[i] < 0:
        # print(lst[i])
        continue  # Also use break....
    else:
        print(lst[i])

