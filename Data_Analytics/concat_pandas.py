import pandas as pd

school1 = pd.read_excel('school1data.xlsx')
school2 = pd.read_excel('school2data.xlsx')
school3 = pd.read_excel('school3data.xlsx')
# print(school1.head())
# print(school2.head())
# print(school3.head())

final = pd.concat([school1 , school2 , school3],ignore_index=False, axis=0)
print(final)
final.to_csv('studentrecord.csv', index=False)