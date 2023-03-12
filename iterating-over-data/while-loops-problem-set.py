# While Loops - id: 31402b5a-5d5a-409f-b5cd-a5c1a7f845d7
# How many times will the body of this while loop run?
counter = 0
while counter < 5:
    print('in the loop body')
    counter += 1

# Answer: 5

# While Loops - id: ce90bffc-5966-4486-8c2f-4d1d10ca58d3
# How many times will the body of this while loop run?
counter = 4
while counter >= 0:
    print('in the loop body')
    counter -= 1

# Answer: 5

# While Loops - id: 5fa25950-37c3-48d9-ae6c-81d41d85e85a
# How many times will the body of this while loop run?
# counter = 0
# while counter < 10:
#     print('in the loop body')

#     if counter < 5:
#         continue

#     counter += 1

# Answer: it runs forever

# While Loops - id: 9401f1e3-778d-4559-a1ef-dee071d4db90
# How many times will the body of this while loop run?
import random

num = random.randint(1, 10)
while num <= 5:
    print('in the loop body')
    num = random.randint(1, 10)

# Answer: impossible to predict

# While Loops - id: 9016d79a-4d74-459f-a714-ca38bf9a176c
# How many times will the body of this while loop run?
while counter < 5:
    print('in the loop body')
    counter += 1

# Answer: 0

# While Loops - id: 0a8cfa41-b770-4e80-8af0-f4d5127c8424
# Which of the for loops below is equivalent to this while loop?
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# Answer:
for counter in range(5):
    print(counter)

# While Loops - id: c90cd73b-bb1d-4f6c-9027-c9db928c199e
# Which of the for loops below is equivalent to this while loop?
counter = 4
while counter >= 0:
    print(counter)
    counter -= 1

# Answer:
for counter in range(4, -1, -1):
  print(counter)

# While Loops - id: 74aac94d-ae5d-40f3-ba50-b8e4c0c2d255
# Which of the for loops below is equivalent to this while loop?
counter = 0
cats = ['Grumpy Cat', 'Garfield', 'Lil Bub', 'Maru', 'Keyboard Cat', 'Hello Kitty']
while counter < len(cats):
    print(cats[counter])
    counter += 1

# Answer:
cats = ['Grumpy Cat', 'Garfield', 'Lil Bub', 'Maru', 'Keyboard Cat', 'Hello Kitty']
for cat in cats:
  print(cat)

# While Loops - id: 879e5790-de4c-4a51-ac38-0330ffb98a67
# Reorder the lines of code below to produce a while loop that runs forever with the following behavior:

# - Prompt the user for input.
# - Ignore the input if the user enters 'skip.'
# - End the loop if the user enters 'done.'
# - Otherwise, print a message telling the user what they input.

# Assume that each line would be indented correctly.

# Answer:
# while True:
#   user_input = input('enter input: ')
#   if user_input == 'done':
#     break
#   elif user_input == 'skip':
#     continue
#   print(f'you entered {user_input}')

# While Loops - id: f44b4f27-82e7-4545-a4d0-766e307971b1
# Let's compare while loops and for loops. Which of the following situations are handled more appropriately with a while loop, compared to a for loop?

# Answer:
# Looping until a condition changes
# Performing an action an indeterminate number of times
# Iterating over the values in a list or dictionary in an arbitrary order
# Looping until a user enters certain data
