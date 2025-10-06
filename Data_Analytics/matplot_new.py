import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y,marker='o')
plt.show()


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.barh(x,y)

plt.show()


x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y,marker='*',color='pink')
plt.show()

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()


# Sample data
categories = ["A", "B", "C", "D", "E"]
values1 = [10, 24, 36, 40, 18]   # First dataset
values2 = [5, 15, 20, 10, 12]    # Second dataset

# Bar chart with stacking
x = np.arange(len(categories))

plt.bar(categories, values1, label="Dataset 1")
plt.bar(categories, values2, bottom=values1, label="Dataset 2")  # stack on top

# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Stacked Column Chart")
plt.legend()

plt.show()


# Sample data
categories = ["A", "B", "C", "D", "E"]
dataset1 = [10, 24, 36, 40, 18]
dataset2 = [5, 15, 20, 10, 12]
dataset3 = [7, 10, 15, 5, 8]

# X-axis positions
x = np.arange(len(categories))

# Plot stacked bars
plt.bar(x, dataset1, label="Dataset 1")
plt.bar(x, dataset2, bottom=dataset1, label="Dataset 2")
plt.bar(x, dataset3, bottom=np.array(dataset1) + np.array(dataset2), label="Dataset 3")


# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Stacked Column Chart")
plt.xticks(x, categories)  # show category labels on X-axis
plt.legend()
plt.grid()
# Show chart
plt.show()'''

# Categories
categories = ["A", "B", "C", "D", "E"]

# Three datasets
dataset1 = [10, 24, 36, 40, 18]
dataset2 = [5, 15, 20, 10, 12]
dataset3 = [7, 10, 15, 5, 8]

# X positions
x = np.arange(len(categories))
width = 0.25  # width of each bar

# Plot side-by-side (clustered)
plt.bar(x - width, dataset1, width, label="Dataset 1")
plt.bar(x, dataset2, width, label="Dataset 2")
plt.bar(x + width, dataset3, width, label="Dataset 3")

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Clustered (Grouped) Bar Chart")
plt.xticks(x, categories)  # show category labels on X-axis
plt.legend()

plt.show()













