"""
#######################
# Selection in Pandas #
#######################

# Read datasets:
df = sns.load_dataset("dataset_name")
df.head() // It prints the first 5 elements.
df.index // It prints total number of columns and columns info.
df[0:13] // # It prints index from 0 to 13, excluding index 13.
df.drop() // Drop specified labels from rows or columns.
            Remove rows or columns by specifying label names and corresponding
            axis, or by specifying directly index or column names. When using a
            multi-index, labels on different levels can be removed by specifying
            the level. See the :ref:`user guide <advanced.shown_levels>`
            for more information about the now unused levels.

            Parameters
            ----------
            labels : single label or list-like
                Index or column labels to drop. A tuple will be used as a single
                label and not treated as a list-like.
            axis : {0 or 'index', 1 or 'columns'}, default 0
                Whether to drop labels from the index (0 or 'index') or
                columns (1 or 'columns').
            index : single label or list-like
                Alternative to specifying axis (``labels, axis=0``
                is equivalent to ``index=labels``).
            columns : single label or list-like
                Alternative to specifying axis (``labels, axis=1``
                is equivalent to ``columns=labels``).
            level : int or level name, optional
                For MultiIndex, level from which the labels will be removed.
            inplace : bool, default False
                If False, return a copy. Otherwise, do operation
                inplace and return None.
            errors : {'ignore', 'raise'}, default 'raise'
                If 'ignore', suppress error and only existing labels are
                dropped.


# Pandas Data Framework:
A data frame is not the same as a data series.
Data framework is the data type that contains multidimensional array and index information but
data series is the data type that contains 1-D array and index information.
That's why the data framework is shown [[]] but the data series is shown [].
The data framework is actually a dataset variable that takes a list within it!

Example:
df["age"].head() // This statement is DATA SERIES.
df[["age"]].head() // This statement is DATA FRAMEWORK.

col_names = ["age", "adult_male", "alive"]
df[col_names].head() // This statement is DATA FRAMEWORK.

# If we want to remove, access, or perform operations on specific cells in a table,
# we use a structure called 'loc':

df.loc[:, df.columns.str.contains("age")].head()

"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())

print(df.index)  # RangeIndex(start=0, stop=891, step=1)

print(df[0:13])
#     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0          0       3    male  22.0  ...   NaN  Southampton     no  False
# 1          1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2          1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3          1       1  female  35.0  ...     C  Southampton    yes  False
# 4          0       3    male  35.0  ...   NaN  Southampton     no   True
# 5          0       3    male   NaN  ...   NaN   Queenstown     no   True
# 6          0       1    male  54.0  ...     E  Southampton     no   True
# 7          0       3    male   2.0  ...   NaN  Southampton     no  False
# 8          1       3  female  27.0  ...   NaN  Southampton    yes  False
# 9          1       2  female  14.0  ...   NaN    Cherbourg    yes  False
# 10         1       3  female   4.0  ...     G  Southampton    yes  False
# 11         1       1  female  58.0  ...     C  Southampton    yes   True
# 12         0       3    male  20.0  ...   NaN  Southampton     no   True
#
# [13 rows x 15 columns]

# Delete index 0 in the table.
print(df.drop(0, axis=0).head())
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
# 4         0       3    male  35.0  ...   NaN  Southampton     no   True
# 5         0       3    male   NaN  ...   NaN   Queenstown     no   True
#
# [5 rows x 15 columns]


delete_indexes = [1, 3, 5, 7]
print(df.drop(delete_indexes, axis=0).head(10))
#     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0          0       3    male  22.0  ...   NaN  Southampton     no  False
# 2          1       3  female  26.0  ...   NaN  Southampton    yes   True
# 4          0       3    male  35.0  ...   NaN  Southampton     no   True
# 6          0       1    male  54.0  ...     E  Southampton     no   True
# 8          1       3  female  27.0  ...   NaN  Southampton    yes  False
# 9          1       2  female  14.0  ...   NaN    Cherbourg    yes  False
# 10         1       3  female   4.0  ...     G  Southampton    yes  False
# 11         1       1  female  58.0  ...     C  Southampton    yes   True
# 12         0       3    male  20.0  ...   NaN  Southampton     no   True
# 13         0       3    male  39.0  ...   NaN  Southampton     no  False
#
# [10 rows x 15 columns]

"""
To save on 'df' =>
- Option 1 (The 'inplace' parameter is commonly used):
  df.drop(delete_indexes, axis=0, inplace=True)

- Option 2:
  df = df.drop(delete_indexes, axis=0).head(10) 
"""

"""
Note! => df["index_name"] = df.index_name
      => df.index // RangeIndex(...)
      
*************************************
* To convert a variable to an index * 
*************************************

- Option 1:

df.index = df["index_name"]
df.drop("index_name", axis=1)

- Option 2:

// We sent a value from variables to an index, 
// and then sent a value from the index back to the variables.
df.reset_index().head()
df = df.reset_index()
df.head()

*************************************
* To convert a index to an variable * 
*************************************

df["new_index"] = df.index
"""

#  pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
print(df.head())

print(type(df["age"]))  # <class 'pandas.core.series.Series'>

print(type(df[["age"]]))  # <class 'pandas.core.frame.DataFrame'>

col_names = ["age", "adult_male", "alive"]
print(type(df[col_names]))  # <class 'pandas.core.frame.DataFrame'>

df["age2"] = df["age"] ** 2
print(df.head())
#    survived  pclass     sex   age  sibsp  ...  deck  embark_town alive  alone    age2
# 0         0       3    male  22.0      1  ...   NaN  Southampton    no  False   484.0
# 1         1       1  female  38.0      1  ...     C    Cherbourg   yes  False  1444.0
# 2         1       3  female  26.0      0  ...   NaN  Southampton   yes   True   676.0
# 3         1       1  female  35.0      1  ...     C  Southampton   yes  False  1225.0
# 4         0       3    male  35.0      0  ...   NaN  Southampton    no   True  1225.0
#
# [5 rows x 16 columns]

df["age3"] = df["age"] / df["age2"]
print(df.head())
#    survived  pclass     sex   age  ...  alive  alone    age2      age3
# 0         0       3    male  22.0  ...     no  False   484.0  0.045455
# 1         1       1  female  38.0  ...    yes  False  1444.0  0.026316
# 2         1       3  female  26.0  ...    yes   True   676.0  0.038462
# 3         1       1  female  35.0  ...    yes  False  1225.0  0.028571
# 4         0       3    male  35.0  ...     no   True  1225.0  0.028571
#
# [5 rows x 17 columns]

"""You can remove columns that correspond to the given list in our main list by providing it as a parameter to the 
'drop()' method."""
# col_names = ["age", "adult_male", "alive"]
print(df.drop(col_names, axis=1).head())  # Row: axis=0, Col: axis=1
#    survived  pclass     sex  sibsp  ...  embark_town  alone    age2      age3
# 0         0       3    male      1  ...  Southampton  False   484.0  0.045455
# 1         1       1  female      1  ...    Cherbourg  False  1444.0  0.026316
# 2         1       3  female      0  ...  Southampton   True   676.0  0.038462
# 3         1       1  female      1  ...  Southampton  False  1225.0  0.028571
# 4         0       3    male      0  ...  Southampton   True  1225.0  0.028571
#
# [5 rows x 14 columns]


'''
Select all columns whose names start with 'age':
'''
print(df.loc[:, df.columns.str.contains("age")].head())
#     age    age2      age3
# 0  22.0   484.0  0.045455
# 1  38.0  1444.0  0.026316
# 2  26.0   676.0  0.038462
# 3  35.0  1225.0  0.028571
# 4  35.0  1225.0  0.028571

'''
Use '~' for the opposite:
'''
print(df.loc[:, ~df.columns.str.contains("age")].head())
#    survived  pclass     sex  sibsp  ...  deck  embark_town alive  alone
# 0         0       3    male      1  ...   NaN  Southampton    no  False
# 1         1       1  female      1  ...     C    Cherbourg   yes  False
# 2         1       3  female      0  ...   NaN  Southampton   yes   True
# 3         1       1  female      1  ...     C  Southampton   yes  False
# 4         0       3    male      0  ...   NaN  Southampton    no   True
#
# [5 rows x 14 columns]
