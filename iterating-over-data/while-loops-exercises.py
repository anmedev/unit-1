# While Loops - id: AJC4nw
# Fix this loop so it loops while i is less than 5 .
# def loop_until_five():
#     i = 0
#     while False:
#         i += 1
#     return i
# result = loop_until_five()

# Answer:
def loop_until_five():
    i = 0
    while i < 5:
        i += 1
    return i
result = loop_until_five()
print(result)

# While Loops - id: jMroBQ
# Think about the function named loop_until_five() from the previous question. What value does loop_until_five() return?

# Answer: 5

# While Loops - id: UZgKoW
# Which of these loop table options most accurately describes this loop?
i = 0
result = None

while i < 5:
    if (i % 2) == 0:
        result = True
    else:
        result = False
    i += 1

# Answer: Loop Table Durian -- see exercise for loop table option

# While Loops - id: SLx1UM
# The function look_for_treasure has an error in it! look_for_treasure should exit after we find treasure. Add in the break keyword in the right location so the test passes.

import random


def check_if_treasure(item):
    is_treasure = random.randrange(100) < 25
    # The line below uses the ternary operator.
    return "Treasure!" if is_treasure else item + 1


def look_for_treasure():
    i = 0

    while True:
        if i == "Treasure!":
            print("We found treasure instead of a number!")
            print("Let's leave while we can.")
        print(f"Counting: i is {i}")
        i = check_if_treasure(i)

    print("I broke out of the loop!")
    return "I'm free!"

# Answer:
import random

def check_if_treasure(item):
  is_treasure = random.randrange(100) < 25 # This will evaluate to True or False.
    # The line below uses the ternary operator.
  return "Treasure!" if is_treasure else item + 1

def look_for_treasure():
  i = 0
  while True:
    if i == "Treasure!":
      print("We found treasure instead of a number!")
      print("Let's leave while we can.")
      break
    print(f"Counting: i is {i}")
    i = check_if_treasure(i)
  print("I broke out of the loop!")
  return "I'm free!"
print(look_for_treasure())
