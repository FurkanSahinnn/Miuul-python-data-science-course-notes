"""
#########################
# Conditional Selection #
#########################

df[<condition>]

"""
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print(df.head())
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0         0       3    male  22.0  ...   NaN  Southampton     no  False
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
# 4         0       3    male  35.0  ...   NaN  Southampton     no   True
# [5 rows x 15 columns]

print(df[df["age"] > 50].head())
'''
or df[df.age > 50].head()
'''
#     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 6          0       1    male  54.0  ...     E  Southampton     no   True
# 11         1       1  female  58.0  ...     C  Southampton    yes   True
# 15         1       2  female  55.0  ...   NaN  Southampton    yes   True
# 33         0       2    male  66.0  ...   NaN  Southampton     no   True
# 54         0       1    male  65.0  ...     B    Cherbourg     no  False
#
# [5 rows x 15 columns]

print(df[df["age"] > 50].count())
# survived       64
# pclass         64
# sex            64
# age            64
# sibsp          64
# parch          64
# fare           64
# embarked       63
# class          64
# who            64
# adult_male     64
# deck           33
# embark_town    63
# alive          64
# alone          64
# dtype: int64

print(df[df["age"] > 50]["age"].count())  # 64

print(df.loc[df["age"] > 50, "class"].head())
# 6      First
# 11     First
# 15    Second
# 33    Second
# 54     First
# Name: class, dtype: category
# Categories (3, object): ['First', 'Second', 'Third']

print(df.loc[df["age"] > 50, ["class", "age"]].head())
#      class   age
# 6    First  54.0
# 11   First  58.0
# 15  Second  55.0
# 33  Second  66.0
# 54   First  65.0

'''
Note =
If there are multiple conditions, they are enclosed in parentheses.

df.loc[df["age"] > 50 & df["sex"] == "male", ["class", "age"]].head() // Error

df.loc[df["age"] > 50 & (df["sex"] == "male"), ["class", "age"]].head() // Not Error
'''

print(df.loc[df["age"] > 50 & (df["sex"] == "male"), ["class", "age"]].head())
#    class   age
# 0  Third  22.0
# 1  First  38.0
# 2  Third  26.0
# 3  First  35.0
# 4  Third  35.0

print(df.loc[df["age"] > 50
             & (df["sex"] == "male")
             & (df["embark_town"] == "Cherbourg"),
["class", "age", "sex", "embark_town"]].head())
#    class   age     sex  embark_town
# 0  Third  22.0    male  Southampton
# 1  First  38.0  female    Cherbourg
# 2  Third  26.0  female  Southampton
# 3  First  35.0  female  Southampton
# 4  Third  35.0    male  Southampton

df_new = df.loc[df["age"] > 50
                & (df["sex"] == "male")
                & (df["embark_town"] == "Cherbourg"),
["class", "age", "sex", "embark_town"]].head()
print(df_new["embark_town"].value_counts())
# embark_town
# Southampton    4
# Cherbourg      1
# Name: count, dtype: int64
