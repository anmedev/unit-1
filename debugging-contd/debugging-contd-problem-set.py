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
# Answer: Stage is a list of lists. The lists of lists evaluates to: [[False, True, False], [False, True, False], [False, True, False]]. False represents where the cell dies and True represents where the cell lives.

# Debugging Continued - id: 42cc6a3a-e111-4344-ba03-bc4b2730c0d3
# Moira needs the inner for loop to iterate over each of the elements in each of the inner loops. She also needs the vertical position and horizontal position of each of the cells so that she can use those to call count_neighbors for each cell. How can Moira change her code to fix this bug?

# Answer: To fix this code, I changed the inner for loop from for h_pos in range(len(v_pos)) to for h_pos in range(len(stage[v_pos])) so that I could iterate over the elements in the inner loops.

# * Note: stage[h_pos] represents the outer list, which evaluates to [False, False, False] since there are three inner lists inside the outer list.