"""
##################
# Join Operation #
##################

pd.concat([df1, df2], ignore_index = True or False)  // Union Join

pd.concat([df1, df2], ignore_index=False)
#    var1  var2  var3
# 0    14    29    26
# 1    14    26     7
# 2     2     7    10
# 3    12    21     1
# 4     9    29    28
# 0   113   128   125
# 1   113   125   106
# 2   101   106   109
# 3   111   120   100
# 4   108   128   127

pd.concat([df1, df2], ignore_index=True)
#    var1  var2  var3
# 0    16    11     2
# 1    10    23    28
# 2    14     2    25
# 3    17    15     6
# 4    11    17     1
# 5   115   110   101
# 6   109   122   127
# 7   113   101   124
# 8   116   114   105
# 9   110   116   100

pd.concat([df1, df2], ignore_index=False, axis=0) // Default parameter

"""

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

print(df1.head())
#    var1  var2  var3
# 0     9    12    15
# 1    15    16     8
# 2    19     4    10
# 3     2    25     4
# 4    27    22    16

print(df2.head())
#    var1  var2  var3
# 0   108   111   114
# 1   114   115   107
# 2   118   103   109
# 3   101   124   103
# 4   126   121   115


print(pd.concat([df1, df2]))
#    var1  var2  var3
# 0    14    29    26
# 1    14    26     7
# 2     2     7    10
# 3    12    21     1
# 4     9    29    28
# 0   113   128   125
# 1   113   125   106
# 2   101   106   109
# 3   111   120   100
# 4   108   128   127

print(pd.concat([df1, df2], ignore_index=True))
#    var1  var2  var3
# 0    16    11     2
# 1    10    23    28
# 2    14     2    25
# 3    17    15     6
# 4    11    17     1
# 5   115   110   101
# 6   109   122   127
# 7   113   101   124
# 8   116   114   105
# 9   110   116   100

df1 = pd.DataFrame({'employees': ['join', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

print(pd.merge(df1, df2))
#   employees        group  start_date
# 0    dennis  engineering        2014
# 1      mark  engineering        2010
# 2     maria           hr        2019

print(pd.merge(df1, df2, on="employees"))
#   employees        group  start_date
# 0    dennis  engineering        2014
# 1      mark  engineering        2010
# 2     maria           hr        2019
