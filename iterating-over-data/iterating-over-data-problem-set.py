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