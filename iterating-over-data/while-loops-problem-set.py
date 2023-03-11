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
