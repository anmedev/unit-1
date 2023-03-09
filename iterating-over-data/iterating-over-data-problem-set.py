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

# Iterating Over Data - id: tTFqeV
# Create a function named sum_series that takes two parameters: min_value and max_value. Starting with min_value, add each number in the range from min_value to max_value together. Then return that total. Required: Use a for-loop and range().

# Answer:
def sum_series(min_value, max_value):
  sum = 0
  for num in range(min_value, max_value + 1):
    sum += num
  return sum
print(sum_series(1, 3)) # 6
print(sum_series(2, 4)) # 9
print(sum_series(0, 5)) # 15
print(sum_series(3, 7)) # 25

# Iterating Over Data - id: 1HUR7V
# Create a function named sum_even_nums_series that takes two parameters: min_value and max_value. Starting with min_value, add each even number in the range from min_value to max_value together. Then return that total. Required: Use a for-loop.

# Answer:
def sum_even_nums_series(min_value, max_value):
  sum = 0
  for num in range(min_value, max_value + 1):
    if num % 2 == 0:
      sum += num
  return sum
print(sum_even_nums_series(1, 3)) # 2
print(sum_even_nums_series(2, 4)) # 6
print(sum_even_nums_series(0, 5)) # 6
print(sum_even_nums_series(3, 7)) # 10

# Iterating Over Data - id: NkbCNAWCF
# Create a function named find_adults. This function has one parameter, people, which is a dictionary. Each key is a string that holds the name of a person.
# Each value is an integer that is the age of that person. The function should return a list of all the names of people that are 18 or older. The list can be in any order. If there are no adults in the dictionary, the function should return an empty list.

# Answer:
def find_adults(people):
  adults_list = []
  for name, age in people.items():
    if age >= 18:
      adults_list.append(name)
  return adults_list

print(find_adults({"Jane": 23, "Mateo": 2, "Eduardo": 18, "Elsa": 1, "Alba": 66})) # ['Jane', 'Eduardo', 'Alba']
print(find_adults({"Mateo": 2, "Eduardo": 18, "Elsa": 1})) # ['Eduardo']
print(find_adults({"Mateo": 2, "Elsa": 1})) # []
print(find_adults({})) # []


