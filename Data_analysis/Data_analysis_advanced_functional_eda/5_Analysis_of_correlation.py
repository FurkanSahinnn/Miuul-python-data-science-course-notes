"""
###########################
# Analysis of Correlation #
###########################

Correlation on a statistical basis is the method of finding the relationship between the variables
in terms of the movement of the data.

(Quoted from 'https://www.digitalocean.com')

-> How is the correlation process done in Python?
*  We can use corr() method.

-> What is '-1 <= corr_result <= 1' in the correlation?
*  The corr_result, which is the result of the correlation process, provides us with information about the relationship
   between two variables.
   If the result is greater than 0, it is called 'positive correlation,'
   and if it is less than 0, it is called 'negative correlation'.

-> What is 'Possitive Correlation'?
*  When the value of one variable increases, the value of the other variable also increases.
   The closer the correlation result is to 1, the stronger the relationship between the two variables.

-> What is 'Negative Correlation'?
*  It is when the value of one variable increases while the value of the other variable decreases.
   The closer the correlation result is to -1, the stronger the relationship between the two variables.

-> If approaching 1 in positive correlation increases the relationship between two variables,
   why does approaching -1 in negative correlation decrease it?

*  Because in correlation, positive and negative only indicate the direction of the relationship between variables.
   Approaching 1 shows how similar the behavior of two variables is, while approaching -1 shows how opposite they are.
   Therefore, whether you approach 1 or -1, the result is an increased relationship between the two variables.

    Notes
    --------
    When analyzing a dataset, we do not want to analyze highly correlated variables
    because variables with high correlation exhibit the same behavior, so knowing only one of them is sufficient.

"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = pd.read_csv("datasets/breast_cancer.csv")

# Let's filter out the unwanted variables using the iloc method:
df = df.iloc[:, 1:-1]

# Select numerical variables in the dataset:
num_cols = [col for col in df.columns if df[col].dtypes in [int, float]]
print(num_cols)

# Correlation process:
corr = df[num_cols].corr()
print(corr)

# To visualize the correlation result of the dataset on a heatmap:
sns.set(rc={"figure.figsize": (12, 12)})
sns.heatmap(corr, cmap="RdBu")
# plt.show()

# Removing highly correlated variables:
'''
Since negative and positive high correlations convey the same meaning,
I should first make the correlation result entirely positive. 
To do this, I am using the absolute value function, which is abs().
'''
cor_matrix = df[num_cols].corr().abs()

'''
We don't want duplicate results, so we should remove them from our outcome. We can use numpy.where() method.
The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.()
The deleted results will appear as 'NaN'.
'''
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
print(upper_triangle_matrix)

'''
If we want to delete one of the variables with a 90% similarity ratio, we will do the following:
The term for this similarity ratio is called the 'threshold value.'
'''
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
print(drop_list)

# Look drop_list inside cor_matrix.
print(cor_matrix[drop_list])

# Remove 'drop_list' inside cor_matrix.
df.drop(drop_list, axis=1)


# Let's write a function that encompasses all of these operations and visualize it:
def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        sns.set(rc={"figure.figsize": (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


high_correlated_cols(df[num_cols])
drop_list = high_correlated_cols(df[num_cols], True)
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), True)
