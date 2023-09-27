"""
#########
# NumPy #
#########

-> There are two fundamental reasons for using Numpy:
1. It enables efficient data storage.
2. It enables vector operations. (Operations at high levels)

-> The differences between Numpy and Lists are as follows:
In Numpy, arrays created maintain a common data type for all elements, rather than specifying the data type individually
for each element as in Lists. This means that an operation performed on a list will take longer compared
to the same operation performed on a Numpy array because data types are explicitly defined for each element in Lists.
In short, Numpy enables accomplishing more with less code.

Import library -> # import numpy as np
Creating array -> # np.array([<elements>])
Create zero array -> # np.zeros(shape, dtype=float (optional default is float64), order='C' (optional), *, like=None (optional))
Create random integer elements array -> # np.random.randint(int startElement, int endElement, int len)
Create Special array -> # np.random.normal(int avg, int stdDeviation, (rowSize, colSize))

Numpy Array Attributes:
# ndim = Number of dimensions
# shape = Information of dimension
# size =  Total number of elements
# dtype = The common data type of the elements in an array.

Reshaping:
It enables transforming an n-dimensional array into an m-dimensional array, where (n < m) & (n x m == len(np.array())).
# np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3) // [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# np.array([1, 2, 3, 4, 5, 6, 7]).reshape(3, 3) // Error!

Index Selection:
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[0] // 1 => Index Selection
# a[1:5] // [2, 3, 4, 5] => Slicing Index Selection

# b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b[2, 1] = 10
# print(b) // [[1, 2, 3], [4, 5, 6], [7, 10, 9]]
# b[2, 1] = 10.10 -> Numpy arrays set all elements to a predefined value in an arranged data type for compatibility.
# print(b) // [[1, 2, 3], [4, 5, 6], [7, 10, 9]]

-> Example:
# m = np.array([...])
# m[:, 0] -> Tüm row'ları seç, 0.index'i seç.
# m[1, :] -> Index'i 1 olan row'daki tüm element'leri seç.
# m[0:2, 0:3] -> Row = 0-2'ye ve col = 0-3'ye kadar reshape eder.

Fancy Index:
It is the action of writing an array that holds the indices into a numpy array, which retrieves the
corresponding values.

# np.arange(start, stop<Not include>, step)
# v = np.arange(0, 20, 3)
# print(v) // [ 0  3  6  9 12 15 18]


Numpy Conditions:
# arr_name[] // Select all elements into arr_name array.
# arr_name[<condition>]

Numpy Math Operations:
# np.subtract(arr_name, subNum)
# np.add(arr_name, addNum)
# np.mean(arr_name)
# np.sum(arr_name)
# np.min(arr_name)
# np.max(arr_name)
# np.var(arr_name)
"""

import numpy as np
numpy_array = np.array([1, 2, 3, 4, 5]) # Creating numpy array
print(numpy_array) # [1 2 3 4 5]

int_zero_array = np.zeros(5, dtype=int) # int_zero_array = [0, 0, 0, 0, 0]
print(int_zero_array) # [0 0 0 0 0]

float_zero_array = np.zeros(5, dtype=float)
print(float_zero_array) # [0. 0. 0. 0. 0.]

random_int_array = np.random.randint(5, 20, size=4) # Size = array.len
print(random_int_array) # [12 16 10 16]

random_special_array = np.random.normal(40, 5, (5,6))
print(random_special_array)
# [[39.41185568 28.53714038 45.48422438 32.28239002 35.69900585 40.6414461 ]
#  [39.23512806 39.79787346 40.07382122 32.57398685 46.6887278  42.7703868 ]
#  [38.06923549 47.89617884 43.6236488  37.71272803 31.35157119 44.45769095]
#  [45.10927594 35.70844339 36.60758166 44.62094027 48.11111708 36.02696205]
#  [33.44169761 37.56328005 42.57310045 33.74608218 36.99847471 41.13420199]]

'''
selectRandomInt(0 -> 10(not included))
# fillArray(row = 3, col = 5)
'''
random_special_array = np.random.randint(10, size=(3,5))
print(random_special_array)
# [[1 3 4 7 9]
#  [0 3 1 2 2]
#  [4 9 7 1 9]]

print(numpy_array.ndim) # 1
print(numpy_array.shape) # (5,)
print(numpy_array.size) # 5
print(numpy_array.dtype) # int32

print(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3))
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

v = np.arange(0, 20, 3)
print(v) # [ 0  3  6  9 12 15 18]

fancy_array = np.arange(0, 30, 2)
fancy_index = [2, 5, 10, 1, 6] # Contain index values
print(fancy_array[fancy_index]) # [ 4 10 20  2 12]

v = np.arange(0, 20, 2)
print(v[v > 10]) # [12 14 16 18]
print(v[v < 10]) # [0 2 4 6 8]
print(v[v != 10]) # [ 0  2  4  6  8 12 14 16 18]
print(v[v == 10]) # [10]
print(v[v >= 10]) # [10 12 14 16 18]

v = np.arange(0, 20, 2) # [ 0  2  4  6  8 10 12 14 16 18]
sub = np.subtract(v, 10) # [-10  -8  -6  -4  -2   0   2   4   6   8]
add = np.add(v, 10) # [10 12 14 16 18 20 22 24 26 28]
mean = np.mean(v) # 9.0
sum = np.sum(v) # 90
min = np.min(v) # 0
max = np.max(v) # 18
var = np.var(v) # 33.0

a = np.arange(1, 7)
print(a.reshape(3,2))