# Debugging Continued - id: a7981c89-552e-4587-9133-341aaa4752f3
# 1. What happens when you run Moira's code?
# Answer: When the code is run, it raises an error

# 2. What line is the error on?
# Answer: The error is on line 19 in the "main.py" file

# 3. What type of error is it?
# Answer: It is a TypeError

# 4. Why is the line throwing an error?
# Answer: The line is throwing an error because v_pos is an integer and the code is trying to apply the len() function on it. This will not work because you cannot iterate over an integer.

# Debugging Continued - id: 8c74e298-f8e7-4635-8990-b8cc5791be43
# Before Moira can fix her nested loop, she needs to make sure that she understands the data structure that she's looping over. Read through the provided functions and use debugging tools like print statements to investigate the stage variable that she is working with.

# What is stage?
# Answer: Stage is a list of lists. The lists of lists read as: [[False, True, False], [False, True, False], [False, True, False]]. False represents where the cell dies and True represents where the cell lives.