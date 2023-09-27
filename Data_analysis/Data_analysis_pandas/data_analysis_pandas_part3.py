"""
##############
# iloc & loc #
##############

DataFrame.loc = Label based selection.
Access a group of rows and columns by label(s) or a boolean array.

DataFrame.iloc = Integer based selection.
Access group of rows and columns by integer position(s).


Note :
    df.loc[row, col]
    df.iloc[row, col]

    df.loc[row, col] // col index include
    df.iloc[row, col] // col index exclude

"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())

# iloc:
print(df.iloc[0:3])
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0         0       3    male  22.0  ...   NaN  Southampton     no  False
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
#
# [3 rows x 15 columns]

print(df.iloc[1, 2])  # female

# loc
print(df.loc[0:3])
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0         0       3    male  22.0  ...   NaN  Southampton     no  False
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
#
# [4 rows x 15 columns]

'''
loc = label based selection
iloc = integer based selection

- iloc[row, col] // row and col must be integer or slicing index.
- loc[row , col] // row must be integer or slicing index 
   but col must be string or list that contains string values.
'''
print(df.iloc[0:3, 0:4])
#    survived  pclass     sex   age
# 0         0       3    male  22.0
# 1         1       1  female  38.0
# 2         1       3  female  26.0

print(df.loc[0:3, "age"])
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# Name: age, dtype: float64

col_names = ["age", "alive", "sex"]
print(df.loc[0:3, col_names])
#     age alive     sex
# 0  22.0    no    male
# 1  38.0   yes  female
# 2  26.0   yes  female
# 3  35.0   yes  female
