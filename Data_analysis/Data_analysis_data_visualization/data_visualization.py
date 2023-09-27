"""
########################
# Matplotlib & Seaborn #
########################

##############
# Matplotlib #
##############

Low-level data visualization refers to doing more with less code,
in other words, accomplishing tasks with minimal coding.

# Categorical variable: Column graphic. countplot bar
# Numeric variable: hist, boxplot
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# Categorical Variable Visualization
'''
df["sex"].value_counts().plot(kind='bar')
plt.show()
'''

# Numeric Variable Visualization
'''
plt.hist(df["age"])
plt.show()
'''

'''
plt.boxplot(df["fare"])
plt.show()
'''

# Matplotlib Properties
'''
-----------------------
x = np.array([1, 10])
y = np.array([3, 170])

plt.plot(x, y)
plt.show()
-----------------------
x = np.array([1, 10])
y = np.array([3, 170])

plt.plot(x, y, 'o')
plt.show()
-----------------------
'''

# Marker
'''
markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']
y = np.array([10, 20, 30, 40, 200])
plt.plot(y, marker='o')
plt.show()
'''

# Line
'''
y = np.array([10, 20, 30, 40, 200])
plt.plot(y, linestyle="dashed")
plt.show()
'''

# Multiple Lines
'''
x = np.array([1, 10, 20, 30, 35])
y = np.array([3, 170, 50, 60, 20])
plt.plot(x)
plt.plot(y)
plt.show()
'''

# plt.title("") // Name the main title
# plt.xlabel("") // Name the X-axis
# plt.ylabel("") // Name the Y-axis
# plt.grid() // Add a grip to the graph

############
# Subplots #
############
'''
plt.subplot(row, col, current_col_num)

x = np.array([10, 20, 30, 40])
y = np.array([200, 300, 400, 500])
plt.subplot(1, 2, 1)
plt.title("1")
plt.plot(x, y)


plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)

plt.show()
'''

"""
###########
# Seaborn #
###########

High-level data visualization refers to accomplishing more with less code, 
in other words, achieving tasks with minimal coding.

"""
df = sns.load_dataset("titanic")
'''
sns.countplot(x, y, data)
'''
sns.countplot(x=df["sex"], data=df)
plt.show()
