# Using a For Loop - id: NkOZhxvAK
# True or False: Once a for loop is executed, it cannot be stopped early. It must complete its loop from start to finish.

# Answer: False

# Using a Break Statement - id: 4yWezZDAY
# Looking at the code below, what is the role of the continue statement?
for i in range(33):
  if i % 3 != 0:
    continue
  print(f"{i} is divisible by 3!")

# Answer: The loop checks to see if the current value of i is divisible by 3. If it's not, the continue statement will skip to the next iteration and will not execute the print statement.

# Using a Range - id: VJnx3ZvRt
# Use 2-5 sentences to answer the following questions:

# What is the role of the range function?
# What three arguments does it take?
# Which arguments are required?

# Answer:
# What is the role of the range function? The range function allows us to create a sequence of numbers.

# What three arguments does it take? It takes three arguments: a start value (where the range should start), a stop value (where the range should end -- the stop value is excluded from the range), and a step value (how much the range should increment/decrement by).

# Which arguments are required? Only the start and stop values are required. The step value is optional, with a default value of 1.
