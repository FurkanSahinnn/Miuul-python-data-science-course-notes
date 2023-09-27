"""
###############################
# Analysis of Target Variable #
###############################

The term 'target variable' refers to the name of the column we want to perform operations on.
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

print(df.head())


# docstring
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Provide the names of categorical, numeric, and categorical but cardinal variables in the dataset.

    Parameters
    ----------
    dataframe: dataframe
        The variable names are for the desired dataframe.
    cat_th: int, float
        The class equality value for variables that are numeric but categorical.
    car_th: int, float
        The class equality value for variables that are categorical but cardinal.

    Returns
    -------
    cat_cols: list
        Categorical variable list
    num_cols: list
        Numerical variable list
    cat_but_car: list
        Categorical-structured cardinal variable list

    Notes
    -------
    cat_cols + num_cols + cat_but_car = Total number of variable
    num_but_cat is within cat_cols.

    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

    cat_but_car = [col for col in df.columns
                   if df[col].nunique() > 20 and
                   str(df[col].dtypes) in ["category", "bool", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car


def cat_summary(dataframe, col_name):
    print("############################")
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))


def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)


"""
##############################################################
# Analysis of the Target Variable with Categorical Variables #
##############################################################
"""

# The distribution of survivors by gender =
# The target is the survival status.
print(df.groupby("sex")["survived"].mean())
'''
sex
female    0.742038
male      0.188908
Name: survived, dtype: float64
'''


def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}))


target_summary_with_cat(df, "survived", "pclass")
'''
        TARGET_MEAN
pclass             
1          0.629630
2          0.472826
3          0.242363
'''

# If we want to look all categorical columns:
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
cat_but_car = [col for col in df.columns
               if df[col].nunique() > 20 and
               str(df[col].dtypes) in ["category", "bool", "object"]]
cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

for col in cat_cols:
    target_summary_with_cat(df, "survived", col)
'''
        TARGET_MEAN
sex                
female     0.742038
male       0.188908
          TARGET_MEAN
embarked             
C            0.553571
Q            0.389610
S            0.336957
        TARGET_MEAN
class              
First      0.629630
Second     0.472826
Third      0.242363
       TARGET_MEAN
who               
child     0.590361
man       0.163873
woman     0.756458
            TARGET_MEAN
adult_male             
False          0.717514
True           0.163873
      TARGET_MEAN
deck             
A        0.466667
B        0.744681
C        0.593220
D        0.757576
E        0.750000
F        0.615385
G        0.500000
             TARGET_MEAN
embark_town             
Cherbourg       0.553571
Queenstown      0.389610
Southampton     0.336957
       TARGET_MEAN
alive             
no             0.0
yes            1.0
       TARGET_MEAN
alone             
False     0.505650
True      0.303538
          TARGET_MEAN
survived             
0                 0.0
1                 1.0
        TARGET_MEAN
pclass             
1          0.629630
2          0.472826
3          0.242363
       TARGET_MEAN
sibsp             
0         0.345395
1         0.535885
2         0.464286
3         0.250000
4         0.166667
5         0.000000
8         0.000000
       TARGET_MEAN
parch             
0         0.343658
1         0.550847
2         0.500000
3         0.600000
4         0.000000
5         0.200000
6         0.000000
'''

"""
##############################################################
# Analysis of the Target Variable with Numerical Variables   #
##############################################################
"""
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

cat_but_car = [col for col in df.columns
               if df[col].nunique() > 20 and
               str(df[col].dtypes) in ["category", "bool", "object"]]

cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
num_cols = [col for col in num_cols if col not in cat_cols]

# The age of survivors =
print(df.groupby("survived")["age"].value_counts())
'''
survived  age  
0         21.00    19
          28.00    18
          25.00    17
          18.00    17
          22.00    16
                   ..
1         0.42      1
          0.67      1
          0.92      1
          7.00      1
          80.00     1
Name: count, Length: 142, dtype: int64
'''

# The average age of survivors =
# The target is the survived status.
print(df.groupby("survived")["age"].mean())
'''
survived
0    30.626179
1    28.343690
Name: age, dtype: float64
'''


def target_summary_with_numerical(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n")


target_summary_with_numerical(df, "survived", "age")
'''
                age
survived           
0         30.626179
1         28.343690
'''

for col in num_cols:
    target_summary_with_numerical(df, "survived", col)
'''
                age
survived           
0         30.626179
1         28.343690

               fare
survived           
0         22.117887
1         48.395408
'''