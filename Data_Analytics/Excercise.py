import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = pd.read_excel('Sample_Superstore.xlsx',sheet_name='Orders')
print(x.head().to_string())


grouped = x.groupby(['Category','Sub-Category','Region','Ship Mode'])['Sales'].sum().reset_index()
print(grouped)
grouped.to_csv('mydata.csv')


# Set up the figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sales Distribution by Category, Sub-Category, Region, and Ship Mode', fontsize=16)

# Subplot 1: Sales by Category
cat_sales = grouped.groupby('Category')['Sales'].sum().reset_index()
print(cat_sales)
sns.barplot(x='Category', y='Sales', data=cat_sales, ax=axs[0, 0],color='seagreen')
axs[0, 0].set_title('Sales by Category')

# Subplot 2: Sales by Sub-Category
subcat_sales = grouped.groupby('Sub-Category')['Sales'].sum().reset_index()
sns.barplot(x='Sales', y='Sub-Category', data=subcat_sales, ax=axs[0, 1],color='steelblue')
axs[0, 1].set_title('Sales by Sub-Category')

# Subplot 3: Sales by Region
region_sales = grouped.groupby('Region')['Sales'].sum().reset_index()
sns.barplot(x='Region', y='Sales', data=region_sales, ax=axs[1, 0], color='darkorange')
axs[1, 0].set_title('Sales by Region')

# Subplot 4: Sales by Ship Mode
ship_sales = grouped.groupby('Ship Mode')['Sales'].sum().reset_index()
sns.barplot(x='Sales', y='Ship Mode', data=ship_sales, ax=axs[1, 1],color='mediumpurple')
axs[1, 1].set_title('Sales by Ship Mode')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


grouped=x.groupby(['Category','Sub-Category','Region','Ship Mode'])['Sales'].sum().reset_index()
print(grouped)



# Set up the figure with 2x2 subplots
fig, axs = plt.subplots(3, 4, figsize=(14, 10))
fig.suptitle('Sales Distribution by Category, Sub-Category, Region, and Ship Mode', fontsize=16)

# Subplot 1: Sales by Category
cat_sales = grouped.groupby('Category')['Sales'].sum().reset_index()
print(cat_sales)
sns.barplot(x='Category', y='Sales', data=cat_sales, ax=axs[0, 0],color='seagreen')
axs[0, 0].set_title('Sales by Category')

# Subplot 2: Sales by Sub-Category
subcat_sales = grouped.groupby('Sub-Category')['Sales'].sum().reset_index()
sns.barplot(x='Sales', y='Sub-Category', data=subcat_sales, ax=axs[0, 1],color='steelblue')
axs[0, 1].set_title('Sales by Sub-Category')

# Subplot 3: Sales by Region
region_sales = grouped.groupby('Region')['Sales'].sum().reset_index()
sns.barplot(x='Region', y='Sales', data=region_sales, ax=axs[0, 2], color='darkorange')
axs[0, 2].set_title('Sales by Region')

# Subplot 4: Sales by Ship Mode
ship_sales = grouped.groupby('Ship Mode')['Sales'].sum().reset_index()
sns.barplot(x='Sales', y='Ship Mode', data=ship_sales, ax=axs[0, 3],color='mediumpurple')
axs[0, 3].set_title('Sales by Ship Mode')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])



grouped=x.groupby(['Category','Sub-Category','Region','Ship Mode'])['Profit'].sum().reset_index()
print(grouped)




# Subplot 1: Sales by Category
cat_sales = grouped.groupby('Category')['Profit'].sum().reset_index()

sns.barplot(x='Category', y='Profit', data=cat_sales, ax=axs[1, 0],color='seagreen')
axs[1, 0].set_title('profit by Category')

# Subplot 2: Sales by Sub-Category
subcat_sales = grouped.groupby('Sub-Category')['Profit'].sum().reset_index()
sns.barplot(x='Profit', y='Sub-Category', data=subcat_sales, ax=axs[1, 1],color='steelblue')
axs[1,1].set_title('Profit by Sub-Category')

# Subplot 3: Sales by Region
region_sales = grouped.groupby('Region')['Profit'].sum().reset_index()
sns.barplot(x='Region', y='Profit', data=region_sales, ax=axs[1, 2], color='darkorange')
axs[1, 2].set_title('Profit by Region')

# Subplot 4: Sales by Ship Mode
ship_sales = grouped.groupby('Ship Mode')['Profit'].sum().reset_index()
sns.barplot(x='Profit', y='Ship Mode', data=ship_sales, ax=axs[1, 3],color='mediumpurple')
axs[1, 3].set_title('Profit by Ship Mode')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])


grouped= x.groupby(['Category','Sub-Category','Region','Ship Mode'])['Quantity'].sum().reset_index()





# Subplot 1: Sales by Category
cat_sales = grouped.groupby('Category')['Quantity'].sum().reset_index()

sns.barplot(x='Category', y='Quantity', data=cat_sales, ax=axs[2, 0],color='seagreen')
axs[2, 0].set_title('Quantity by Category')

# Subplot 2: Sales by Sub-Category
subcat_sales = grouped.groupby('Sub-Category')['Quantity'].sum().reset_index()
sns.barplot(x='Quantity', y='Sub-Category', data=subcat_sales, ax=axs[2, 1],color='steelblue')
axs[2, 1].set_title('Profit by Sub-Category')

# Subplot 3: Sales by Region
region_sales = grouped.groupby('Region')['Quantity'].sum().reset_index()
sns.barplot(x='Region', y='Quantity', data=region_sales, ax=axs[2, 2], color='darkorange')
axs[2, 2].set_title('Quantity by Region')

# Subplot 4: Sales by Ship Mode
ship_sales = grouped.groupby('Ship Mode')['Quantity'].sum().reset_index()
sns.barplot(x='Quantity', y='Ship Mode', data=ship_sales, ax=axs[2,3],color='mediumpurple')
axs[2,3].set_title('Quantity by Ship Mode')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

