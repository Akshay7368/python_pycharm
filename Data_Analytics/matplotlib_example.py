import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv('ipl_matches_2008_2022.csv')
df2 = pd.read_csv('ipl_ball_by_ball_2008_2022.csv')
#print(df1.head().to_string())
#print(df2.head().to_string())


output = pd.merge(df1,df2, on='id', how='left')
#print(output.head().to_string())
#print(output.shape)

batsman_wise_run = output.groupby('batter')['batsman_run'].sum().sort_values(ascending=False).reset_index().head(10)
#print(batsman_wise_run)
#plt.bar(batsman_wise_run['batter'],batsman_wise_run['batsman_run'])
#plt.title('Records')
#plt.xlabel('Batsmen')
#plt.ylabel('Total Runs')
#plt.show()


# Sample DataFrame
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [200, 240, 300, 280, 350, 400]
}

df = pd.DataFrame(data)
'''# Plot line graph
plt.plot(df["Month"], df["Sales"], marker='D', color='Green', linestyle='-', linewidth=2)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
'''

plt.barh(df["Month"], df["Sales"], color='Yellow')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
#plt.grid(True)
plt.show()