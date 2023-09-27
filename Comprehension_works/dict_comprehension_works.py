import seaborn as sns

dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
print(dictionary.keys())  # dict_keys(['a', 'b', 'c', 'd'])
print(dictionary.values())  # dict_values([1, 2, 3, 4])
print(dictionary.items())  # dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# {k: v} -> Here, k = key, v = value represent. You will enter (k, v) as an index.
print({k: v ** 2 for (k, v) in dictionary.items()})  # {'a': 1, 'b': 4, 'c': 9, 'd': 16}
print({k.upper(): v for (k, v) in dictionary.items()})  # {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print({k.upper(): v * 2 for (k, v) in dictionary.items()})  # {'A': 2, 'B': 4, 'C': 6, 'D': 8}

# Soru-1: They want to add the squares of even numbers to a dictionary.
numbers = range(10)
print({n: n ** 2 for n in numbers if n % 2 == 0})  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Read datasets
df = sns.load_dataset("car_crashes")
print(df.columns)  # Index(['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium',
# 'ins_losses', 'abbrev'], dtype='object')

# Soru-2: Convert the variable names (column names) in a data set to uppercase.
print([data for data in df.columns])  # ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous',
# 'ins_premium', 'ins_losses', 'abbrev']
print([data.upper() for data in df.columns])  # ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
# 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

df.columns = [data.upper() for data in df.columns]
print(df.columns)  # Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM',
# 'INS_LOSSES', 'ABBREV'], dtype='object')
print([data for data in df.columns])  # ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
# 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

# Soru-3: Add FLAG to the beginning of variables with "INS" in their name, and add NO_FLAG to the others.
print(["FLAG_" + data if "INS" in data else "NO_FLAG_" + data for data in
       df.columns])  # ['NO_FLAG_TOTAL', 'NO_FLAG_SPEEDING', 'NO_FLAG_ALCOHOL', 'NO_FLAG_NOT_DISTRACTED',
# 'NO_FLAG_NO_PREVIOUS', 'FLAG_INS_PREMIUM', 'FLAG_INS_LOSSES', 'NO_FLAG_ABBREV']

# Soru-4: Create a dictionary with the key as a string and the value as a list as shown below.
df = sns.load_dataset("car_crashes")
select_numbers = [num for num in df.columns if df[num].dtype != "O"]
print(select_numbers)  # ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses']
aggregate_list = ["mean", "min", "max", "sum"]

new_dict = {col: aggregate_list for col in select_numbers}
print(df[select_numbers].head())

# total  speeding  alcohol  ...  no_previous  ins_premium  ins_losses
# 0   18.8     7.332    5.640  ...       15.040       784.55      145.08
# 1   18.1     7.421    4.525  ...       17.014      1053.48      133.93
# 2   18.6     6.510    5.208  ...       17.856       899.47      110.35
# 3   22.4     4.032    5.824  ...       21.280       827.34      142.39
# 4   12.0     4.200    3.360  ...       10.680       878.41      165.63

print(df[select_numbers].agg(new_dict))

# total    speeding  ...   ins_premium   ins_losses
# mean   15.790196    4.998196  ...    886.957647   134.493137
# min     5.900000    1.792000  ...    641.960000    82.750000
# max    23.900000    9.450000  ...   1301.520000   194.780000
# sum   805.300000  254.908000  ...  45234.840000  6859.150000
