# Iterating Over Data - id: N1iCy1fCF
# Given this dictionary...
my_profile = {"icecream_flavor": "chocolate", "has_siblings": True}
# Which of the loops below will produce the following output?
# icecream_flavor
# has_siblings

# Answer:
for x in my_profile:
    print(x)

for x in my_profile.keys():
    print(x)

# Iterating Over Data - id: NyhIeJG0K
# Given this dictionary...
my_profile = {"icecream_flavor": "chocolate", "has_siblings": True}
# Which of the loops below will produce the following output?
# chocolate
# True

# Answer:
for x in my_profile:
    print(my_profile[x])

for x, y in my_profile.items():
    print(y)

# Iterating Over Data - id: EkdvU6Z0K
# Create a function named sum_list that takes a parameter list (a list of integers). Iterate through the list and sum up each integer. Then return the total.

# Answer:
def sum_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum
print(sum_list([1,2,3,4])) # 10

# Iterating Over Data - id: hGaZd5
# Create a function named listify_series that takes one parameter max_value (an integer). Append each number in the range from 1 to max_value to a list. Then return that list. Required: Use a for-loop and range().

# Answer:
def listify_series(max_value):
  final_list = []
  for num in range(1, max_value + 1):
    final_list.append(num)
  return final_list
print(listify_series(3)) # [1, 2, 3]
print(listify_series(5)) # [1, 2, 3, 4, 5]
print(listify_series(10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Iterating Over Data - id: 7wMVtj
# Create a function named sum_series that takes one parameter max_value (an integer). Starting with 1, add each number in the range from 1 to max_value together. Then return that total. Required: Use a for-loop and range().

# Answer:
def sum_series(max_value):
  sum = 0
  for num in range(1, max_value + 1):
    sum += num
  return sum
print(sum_series(3)) # 6
print(sum_series(5)) # 15
print(sum_series(10)) # 55




