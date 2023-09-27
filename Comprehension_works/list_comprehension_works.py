salaries = [1000, 2000, 3000, 4000, 5000]

# Everything will be written inside this => []

# The structure inside the for loop must always be on the left, and if-else statements within a for loop should be on
# the right, if used!
print([salary * 2 for salary in salaries if salary < 3000])  # [2000, 4000]

# If you are going to use a for loop, the for loop is on the right, and its contents are on the left.
print([salary * 2 for salary in salaries])
# This is equivalent to = for salary in salaries: salary * 2, Output = [2000, 4000, 6000, 8000, 10000]

# If you are going to use if-else and for together, the for loop must definitely come to the far right,
# while the if statement must be on the left of the for loop.
# The statement inside the for loop must be on the far left. For example:
print([salary * 2 if salary < 3000 else salary * 3 for salary in salaries])  # [2000, 4000, 9000, 12000, 15000]

# Example:
students = ["John", "Mark", "Venessa", "Mariam"]  # All students.
students_no = ["John", "Venessa"]  # Unwanted students.

print([student for student in students if student not in students_no])  # ['Mark', 'Mariam']
