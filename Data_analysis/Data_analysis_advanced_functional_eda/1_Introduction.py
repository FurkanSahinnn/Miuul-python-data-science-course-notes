"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("titanic")

df.head() # the first 5 observation units
df.tail() # the last 5 observation units
df.shape  # the row and column numbers
df.info() # variables, missing values, types of variables
df.dtypes # types of the variables
df.columns # names of variables
df.index # index information
df.isnull().values.any() # checks whether there are any missing values
df.isnull().sum() # missing values of variable
df.describe().T # some statistics such as mean, count, sum, etc.

"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

"""
df.shape  -> Provides row and column information
df.columns  -> Variable names
df.describe().T  -> Describing numerical variables
df.isnull().values.any()  -> Is there any missing value
df.isnull().sum()  -> Answers how many missing values are there in the dataset
"""


# We can write a function like this to present information
# about the dataset we've loaded more elegantly:
def check_df(dataframe, head=5):
    print("##### Shape #####")
    print(dataframe.shape)
    print("##### Types #####")
    print(dataframe.dtypes)
    print("##### Head #####")
    print(dataframe.head(head))
    print("##### Tail #####")
    print(dataframe.tail(head))
    print("##### NA #####")
    print(dataframe.isnull().sum())
    print("##### Quantiles #####")
    print(dataframe.describe([0, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

df = sns.load_dataset("tips")
check_df(df)
