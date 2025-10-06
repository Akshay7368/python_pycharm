# S= set()
# print(dir(set))
#


# S1 =set()
# S1.add(3)
# S1.add(4)
# S1.add(5)
# S1.add(8)
# S1.add(3)
# print(S1)

# S2 = {'a', 'c', 'd', 'e', }
# S3 = {'t', 'a', 'z', 'c', }
# S4 = {'a', 'r', 'w', 'c', }
# Ans = S2.union(S3)
# print(Ans)
# Ans = S2.union(S3,S4)
# print(Ans)
# Ans2 = S2|S3|S4
# print(Ans2)


# Ans3 = S2.intersection(S3)
# print(Ans3)

# Ans3 = S2 & S3 & S4
# print(Ans3)

# Ans4 = S2 - S3
# print(Ans4)

# Ans4 = S2.difference(S3)
# print(Ans4)
#
# Ans5 = S4.difference(Ans4)
# print(Ans5)
#
#
# # symmetric difference
# Ans6 = S2 ^ S3
# print(Ans6)

# S = {2, 5, 7, 9, 0, 3}
# print(S)
# S.pop()
# print(S)
# S.discard(3)
# print(S)
# S.remove(7)
# print(S)


# if no value matches it prints True, if matches it gives output as false
# S = {'A', 'B', 'C'}
# S1 = {'S', 'R', 'C'}
# print(S.isdisjoint(S1))

# Subset - if all values in S present in S1 it will give value as True,else false
# Superset Vice - versa
# S = {'A', 'B', 'C', 'D', 'E'}
# S1 = {'S', 'R', 'C', 'A'}
# print(S.issubset(S1))
# print(S.issuperset(S1))

#
# S = {'A', 'B', 'C'}
# S1 = {'A', 'Z', 'Y', 'R'}
# print(S)
# print(S1)
# S.update(S1)
# print(S)
# print(S1)

S = {2,4,5,6,7,8}
# S.add(12)
# print(S)
S1 = {1,3,4,7,9,13,5}
# union = (S.union(S1))
# print(union)
# intersection = (S.intersection(S1))
# print(intersection)
diff = S.difference(S1)
print(diff)
sym_diff = S.symmetric_difference(S1)
print(sym_diff)

# S.pop()
# print(S)
# S.remove(8)
# print(S)
# S.discard(6)
# print(S)





