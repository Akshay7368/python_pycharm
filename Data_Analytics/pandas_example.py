import pandas as pd
'''
st_id = {'ID':[1,2,3,4,5], 'Name':['A','B','C','D','E']}
print(st_id)
df = pd.DataFrame(st_id)
print(df)
st_id = [[1,'A'],[2,'B'],[3,'C'],[4,'D'],[5,'E']]
df2 = pd.DataFrame(st_id,columns=['student_ID','student_name'],index=['A','B','C','D','E'])
print(df2)

employee_data = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25],

    "name": ["Alice", "Bob", "Charlie", "David", "Eve",
             "Frank", "Grace", "Hannah", "Ian", "Julia",
             "Kevin", "Laura", "Mike", "Nina", "Oscar",
             "Paula", "Quinn", "Rachel", "Steve", "Tina",
             "Uma", "Victor", "Wendy", "Xander", "Yara"],

    "age": [25, 32, 28, 45, 29,
            39, 31, 27, 41, 36,
            30, 34, 33, 26, 38,
            35, 40, 24, 42, 37,
            23, 43, 44, 22, 46],

    "salary": [50000, 60000, 55000, 75000, 52000,
               70000, 58000, 51000, 72000, 68000,
               53000, 62000, 61000, 50500, 69000,
               64000, 73000, 49000, 74000, 66000,
               48000, 76000, 77000, 47000, 78000],

    "location": ["New York", "Los Angeles", "Chicago", "Houston", "Houston",
                 "Houston", "San Antonio", "San Diego", "Dallas", "San Jose",
                 "Austin", "Jacksonville", "Fort Worth", "Columbus", "Houston",
                 "Indianapolis", "Seattle", "Denver", "Washington", "Boston",
                 "El Paso", "Nashville", "Indianapolis", "Memphis", "Denver"]
}

df = pd.DataFrame(employee_data)
print(df)

print(df.head())
print(df.dtypes)
print(df.columns)

df['Bonus'] = df['salary'] * 0.10
print(df)


df['NewSalary'] = df['salary'] + df['Bonus']
print(df)

print(max(df['salary']))


def grade(sal):
    if sal > 75000:
        return "A Grade Employee"
    elif sal<75000 and sal>=50000:
        return "B Grade Employee"
    else:
        return "C Grade Employee"

df['Grade'] = df['NewSalary'].apply(grade)
print(df)



print(df.to_csv("output.csv",index=False))

print(df.describe())
'''

orders = pd.read_excel('Sample_Superstore.xlsx', sheet_name='Orders')
print(orders.shape)
print(orders.info())
print(orders.describe().to_string())
orders['year'] = orders['Order Date'].dt.year
orders['month'] = orders['Order Date'].dt.month
orders['day'] = orders['Order Date'].dt.day
print(orders.head().to_string())

westregion = orders[orders['Region']== 'West'].to_string()
print(westregion)

westregion1 = orders[(orders['Region'] == 'West') & (orders['Sales'] > 5000)]
print(westregion1)

data_2014 = orders[orders['year'] == 2014]
print(data_2014.to_csv('2014_datas.csv',index=False))

data_2015 = orders[orders['year'] == 2015]
print(data_2015.to_csv('2015_datas.csv',index=False))

data_2016 = orders[orders['year'] == 2016]
print(data_2016.to_csv('2016_datas.csv',index=False))


output = orders[((orders['Region'] == 'West') & (orders['Sales'] > 2500)) | (orders['Region'] == 'East')]
print(output)