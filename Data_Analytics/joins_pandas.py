import pandas as pd
emdf = pd.read_excel('employee_workbook_data.xlsx', sheet_name='Employees')
depdf = pd.read_excel('employee_workbook_data.xlsx', sheet_name='departments')
locdf = pd.read_excel('employee_workbook_data.xlsx', sheet_name='locations')
regdf = pd.read_excel('employee_workbook_data.xlsx', sheet_name='regions')
condf = pd.read_excel('employee_workbook_data.xlsx', sheet_name='countries')


m1 = pd.merge(emdf,depdf,on='DEPARTMENT_ID', how='left')
m2 = pd.merge(m1,locdf, on='LOCATION_ID',how='left')
m3 = pd.merge(m2,condf, on='COUNTRY_ID', how='left')
final = pd.merge(m3,regdf, on='REGION_ID', how='left')
print(final.to_string())
final.to_csv('Finaloutput.csv', index=False)



