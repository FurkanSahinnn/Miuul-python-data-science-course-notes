"""
##################
# Apply & Lambda #
##################

apply(lambda var: var/10)
"""

import seaborn as sns

df = sns.load_dataset("titanic")

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 3

print(df.head())
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0         0       3    male  22.0  ...   NaN  Southampton     no  False
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
# 4         0       3    male  35.0  ...   NaN  Southampton     no   True
#
# [5 rows x 15 columns]

print(df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head())
#    age  age2  age3
# 0  2.2   4.4   6.6
# 1  3.8   7.6  11.4
# 2  2.6   5.2   7.8
# 3  3.5   7.0  10.5
# 4  3.5   7.0  10.5

print(df["age"].apply(lambda x: x * 2).head())
# 0    44.0
# 1    76.0
# 2    52.0
# 3    70.0
# 4    70.0
# Name: age, dtype: float64

print(df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()))


#           age      age2      age3
# 0   -0.530005 -0.530005 -0.530005
# 1    0.571430  0.571430  0.571430
# 2   -0.254646 -0.254646 -0.254646
# 3    0.364911  0.364911  0.364911
# 4    0.364911  0.364911  0.364911
# ..        ...       ...       ...
# 886 -0.185807 -0.185807 -0.185807
# 887 -0.736524 -0.736524 -0.736524
# 888       NaN       NaN       NaN
# 889 -0.254646 -0.254646 -0.254646
# 890  0.158392  0.158392  0.158392
#
# [891 rows x 3 columns]

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


print(df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head())
#         age      age2      age3
# 0 -0.530005 -0.530005 -0.530005
# 1  0.571430  0.571430  0.571430
# 2 -0.254646 -0.254646 -0.254646
# 3  0.364911  0.364911  0.364911
# 4  0.364911  0.364911  0.364911

df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)
#         age      age2      age3
# 0 -0.530005 -0.530005 -0.530005
# 1  0.571430  0.571430  0.571430
# 2 -0.254646 -0.254646 -0.254646
# 3  0.364911  0.364911  0.364911
# 4  0.364911  0.364911  0.364911


