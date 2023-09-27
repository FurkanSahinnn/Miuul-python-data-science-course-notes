"""
# Pandas Series -> The data type that contains 1-D array and index information.
# Pandas Framework -> The data type that contains multidimensional array and index information.

Create pandas series -> s = pd.Series([...])
Access pandas series indexes -> s.index
Learn pandas series type -> s.dtype
Access length -> s.size
Access dimension info -> s.ndim
Access values -> s.values // Note: This method return numPy array type.

- Displays all the elements of the array from the first index to the entered index.
s.head(num) // num parameter is last index. But it's not include.

- Displays the elements from the specified index to the last index.
s.tail(num) // num value is not include.


# Data Read From File:
pd.read_csv("<file_path>")

"""

import pandas as pd
import seaborn as sns

pandas_series = pd.Series([10, 77, 12, 4, 5])
print(pandas_series)
# 0    10
# 1    77
# 2    12
# 3     4
# 4     5
# dtype: int64

print(pandas_series.index)  # RangeIndex(start=0, stop=5, step=1)

print(pandas_series.dtype)  # int64

print(pandas_series.size)  # 5

print(pandas_series.ndim)  # 1

print(pandas_series.values)  # [10 77 12  4  5]

print(pandas_series.head(3))
# 0    10
# 1    77
# 2    12
# dtype: int64

print(pandas_series.tail(2))
# 3    4
# 4    5
# dtype: int64

df = pd.read_csv("datasets/advertising.csv")
print(df.head())
#    TV  radio  newspaper  sales  Unnamed: 4
# 0   1  230.1       37.8   69.2        22.1
# 1   2   44.5       39.3   45.1        10.4
# 2   3   17.2       45.9   69.3         9.3
# 3   4  151.5       41.3   58.5        18.5
# 4   5  180.8       10.8   58.4        12.9

df = sns.load_dataset("car_crashes")
print(df.head())
#     total  speeding  alcohol  ...  ins_premium  ins_losses  abbrev
# 0   18.8     7.332    5.640  ...       784.55      145.08      AL
# 1   18.1     7.421    4.525  ...      1053.48      133.93      AK
# 2   18.6     6.510    5.208  ...       899.47      110.35      AZ
# 3   22.4     4.032    5.824  ...       827.34      142.39      AR
# 4   12.0     4.200    3.360  ...       878.41      165.63      CA
#
# [5 rows x 8 columns]

print(df.shape)  # (51, 8) // Learn df row and col values.

# print(df.info)

print(df.columns)
# Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
#        'ins_premium', 'ins_losses', 'abbrev'],
#       dtype='object')

print(df.index)  # RangeIndex(start=0, stop=51, step=1)

print(df.describe().T)  # df.describe() is transposed
#                  count        mean         std  ...      50%       75%       max
# total            51.0   15.790196    4.122002  ...   15.600    18.500    23.900
# speeding         51.0    4.998196    2.017747  ...    4.608     6.439     9.450
# alcohol          51.0    4.886784    1.729133  ...    4.554     5.604    10.038
# not_distracted   51.0   13.573176    4.508977  ...   13.857    16.140    23.661
# no_previous      51.0   14.004882    3.764672  ...   13.775    16.755    21.280
# ins_premium      51.0  886.957647  178.296285  ...  858.970  1007.945  1301.520
# ins_losses       51.0  134.493137   24.835922  ...  136.050   151.870   194.780
#
# [7 rows x 8 columns]

# It returns a table that contains true and false.
print(df.isnull())

# It just takes true and false values from within the table and puts these values into numPy array.
print(df.isnull().values)

# If there is true in any of them, return true.
print(df.isnull().values.any())

# It returns the total number of true values in each column.
print(df.isnull().sum())

'''
#######
#Note:#
#######
    
True = 1 and false = 0 so,
true + false are equal to 1
true + true are equal to 2
false + false are equal to 0
'''

# It returns the total quantity of elements in a specific column.
'''
Syntax:

pandas_array["specific_col_name"].count()
'''
df = pd.read_csv("datasets/persona.csv")
print(df["SEX"])  # It returns the column named 'SEX'.
'''
0         male
1         male
2         male
3         male
4         male
         ...  
4995    female
4996    female
4997    female
4998    female
4999    female
Name: SEX, Length: 5000, dtype: object
'''

print(df["SEX"].count())  # 5000

print(df["SEX"].value_counts())  # It groups elements with the same values and returns how many are in each group.
'''
female    2621
male      2379
Name: count, dtype: int64
'''