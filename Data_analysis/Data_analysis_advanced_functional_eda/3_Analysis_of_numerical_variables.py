import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

"""
If you want to see the descriptions (summary statistics) of the 'age' and 'fare' columns in the Titanic dataset:
"""
print(df[["age", "fare"]].describe().T)
'''
count       mean        std   min      25%      50%   75%       max
age   714.0  29.699118  14.526497  0.42  20.1250  28.0000  38.0   80.0000
fare  891.0  32.204208  49.693429  0.00   7.9104  14.4542  31.0  512.3292
'''

"""
If you are going to use list comprehension to select numerical variables in a dataset, 
you can use the following structure as in the categorical variable analysis section:
"""
num_cols = [col for col in df.columns if df[col].dtypes in ["int64", "float64"]]
print(num_cols)
# ['survived', 'pclass', 'age', 'sibsp', 'parch', 'fare']

"""
The above result is actually incorrect, as we may recall from the analysis of categorical variables section. 
There were some special variable types that, although appearing as numerical from the outside,
were actually categorical variables, and they had a special name: 'High cardinality categorical variables.' 
The reason for the mismatch between the desired result and the above result is this. To solve this problem, 
we should also consider removing high cardinality categorical variables. 
To do this, we first need to be aware of the 'cat_cols' structure.
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
print(num_cols)
# ['age', 'fare']


"""
We will not go through the process as shown above every time we receive a dataset; 
instead, we will write an analysis function that includes the structures mentioned above.
"""


def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)


num_summary(df, "age")
'''
count    714.000000
mean      29.699118
std       14.526497
min        0.420000
5%         4.000000
10%       14.000000
20%       19.000000
30%       22.000000
40%       25.000000
50%       28.000000
60%       31.800000
70%       36.000000
80%       41.000000
90%       50.000000
95%       56.000000
99%       65.870000
max       80.000000
Name: age, dtype: float64
'''

# If we want to perform this process for all columns:
for col in num_cols:
    num_summary(df, col)

# If we want to visualize the results of this function:
def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

# If we want to visualize all the columns sequentially:
for col in num_cols:
    num_summary(df, col, plot=True)


"""
Capturing Variables and Generalizing Operations =
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")


# If the number of unique values is less than 10, we will treat it as a categorical variable, and if it is more than 20,
# we will treat it as a high cardinality categorical variable.

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


print(grab_col_names(df))
'''
Observations: 891
Variables: 15
cat_cols: 13
num_cols: 2
cat_but_car: 0
num_but_cat: 4
(['sex', 'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone', 'survived', 'pclass', 
'sibsp', 'parch'], ['age', 'fare'], [])
'''

cat_cols, num_cols, cat_but_car = grab_col_names(df)
