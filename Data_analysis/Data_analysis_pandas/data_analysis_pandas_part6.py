"""
###############
# Pivot Table #
###############

A Pivot Table is a powerful tool for calculating, summarizing, and analyzing data to help you
visualize comparisons, patterns, and trends in your data.

# df.pivot_table(values, index, columns, aggfunc)  // Default agg is mean.

# pd.cut() -> Convert integer variable to categorical variable.
              The cut() method is used to specify the categories into which you want to divide categorical variables.

# pd.qcut() -> Convert integer variable to categorical variable.
               If you don't know the numerical variable at hand and wish to divide it into quartiles for that reason,
               you would use the qcut() method.

"""

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())

print(df.pivot_table("survived", "sex", "embarked"))

print(df.pivot_table("survived", "sex", "embarked", aggfunc="std"))
# embarked         C         Q         S
# sex
# female    0.876712  0.750000  0.689655
# male      0.305263  0.073171  0.174603
# embarked         C         Q         S
# sex
# female    0.331042  0.439155  0.463778
# male      0.462962  0.263652  0.380058

print(df.pivot_table("survived", "sex", ["embarked", "class"]))
# embarked         C                   ...         S
# class        First Second     Third  ...     First    Second     Third
# sex                                  ...
# female    0.976744    1.0  0.652174  ...  0.958333  0.910448  0.375000
# male      0.404762    0.2  0.232558  ...  0.354430  0.154639  0.128302

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
print(df.head())
#    survived  pclass     sex   age  ...  embark_town  alive  alone   new_age
# 0         0       3    male  22.0  ...  Southampton     no  False  (18, 25]
# 1         1       1  female  38.0  ...    Cherbourg    yes  False  (25, 40]
# 2         1       3  female  26.0  ...  Southampton    yes   True  (25, 40]
# 3         1       1  female  35.0  ...  Southampton    yes  False  (25, 40]
# 4         0       3    male  35.0  ...  Southampton     no   True  (25, 40]
#
# [5 rows x 16 columns]

print(df.pivot_table("survived", "sex", ["new_age", "class"]))
# new_age (0, 10]                   ...  (40, 90]
# class     First Second     Third  ...     First    Second     Third
# sex                               ...
# female      0.0    1.0  0.500000  ...  0.961538  0.846154  0.111111
# male        1.0    1.0  0.363636  ...  0.280000  0.095238  0.064516
#
# [2 rows x 15 columns]