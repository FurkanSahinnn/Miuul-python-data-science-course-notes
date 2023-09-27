"""
#####################################
# Analysis of Categorical Variables #
#####################################

A categorical variable is a variable with a set number of groups (gender, colors of the rainbow, brands of cereal),
while a numeric variable is generally something that can be measured (height, weight, miles per hour).

Categorical Variable Types => object, category, bool
Numerical Variable Types => float, int, double

We could see the values of the desired column in a dataset using the following methods:

df["Col_name"].value_counts() -> Returns object containing counts of unique values.
df["Col_name"].unique() -> Finds the unique elements of an array and returns these unique elements as a sorted array.
df["Col_name"].nunique() -> Returns the number of unique values for each column.

print(df["embarked"].value_counts())
'''
embarked
S    644
C    168
Q     77
'''

print(df["embarked"].unique())
'''
Name: count, dtype: int64
['S' 'C' 'Q' nan]
'''

print(df["embarked"].nunique())
'''
3
'''

Detecting categorical variables can become quite challenging when the dataset is very large.
For this reason, advanced categorical variable analysis is employed.
The reason it's called advanced is that it performs more sophisticated operations than the ones mentioned above.

"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")

"""
How do we perform categorical variable analysis using list comprehension?

df["col_name"].dtypes -> It returns the type information of col_name.
str(df["col_name"].dtypes) -> It converts this type information to a string.
str(df["col_name"].dtypes) in ["object"] -> It checks if this string type information exists within another string list.
"""
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "bool", "object"]]
print(cat_cols)
# ['sex', 'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone']

"""
Why do we need other methods for categorical variable analysis when we have list comprehension?

Sometimes or often, column information that appears as a numeric variable, such as int or float, can turn out to be a 
categorical variable when we perform 'df["col_name"].value_counts()'. For example,

df["survived"].value_counts() 
0  549
1  342
Name: survived, dtype: int64

In the example above, although the 'survived' variable may initially appear as numerical in type, it is a categorical 
variable because it contains two classes. It is not quite feasible to perform categorical variable analysis 
accurately on datasets of this kind using list comprehension.

How can we solve this problem?

You can still use list comprehension to solve this.
Let's say it considers numerical variables with less than 10 classes as categorical variables:
"""
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
print(num_but_cat)
#  ['survived', 'pclass', 'sibsp', 'parch']

"""When we have a dataset containing names and ages, the names will be a categorical variable with a very high 
cardinality because they will be unique for each row. These variables are called 'High cardinality categorical 
variables,' which means they have so many classes that they are impractical to measure or explain. You should do 
something that allows you to access non-categorical variables, or in other words, high cardinality categorical 
variables, even though they have a categorical type.

To do this:
"""
cat_but_car = [col for col in df.columns
               if df[col].nunique() > 20 and
               str(df[col].dtypes) in ["category", "bool", "object"]]
print(cat_but_car)
# []

"""
Since cat_cols also includes categorical variables within numerical ones, we need to add them as well:
"""
cat_cols = cat_cols + num_but_cat
print(cat_cols)
# ['sex', 'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone', 'survived', 'pclass',
# 'sibsp', 'parch']

# Note =
'''In this example, the list cat_but_car is empty, so it didn't add anything. However, in a scenario where there are 
high cardinality variables, we need to append the high cardinality variables only on top of the categorical 
variables.
'''

"""If, after the last operation, the user wants us to select only the categorical variables rather than the high 
cardinality ones, we can do the following:
"""
cat_cols = [col for col in cat_cols if col not in cat_but_car]
# ['sex', 'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone']

# This way, we have selected categorical variables that are not high cardinality.

# If we want to select numerical variables from the final state of cat_cols:
num_cols = [col for col in df.columns if col not in cat_cols]
print(num_cols)

"""
If we want to perform all these operations for a specific column in a single function:
"""


def cat_summary(dataframe, col_name):
    print("############################")
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))


for col in cat_cols:
    cat_summary(df, col)

"""
Let's add data visualization capability to the function we've written and make the operations we performed more 
comprehensible on a graph:
"""


def cat_summary(dataframe, col_name, plot=False):
    print("############################")
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


cat_summary(df, "sex", plot=True)

"""
If a countplot encounters a column with a bool type, it will raise an error. To prevent this, we can skip that 
part when a bool type is encountered using an 'if' statement.
"""
for col in cat_cols:
    if df[col].dtypes != "bool":
        cat_summary(df, col, plot=True)

"""
Another solution to the problem above is to change the type when we encounter a bool column.
"""
for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)  # Convert 'bool' to 'int'
    cat_summary(df, col, plot=True)

