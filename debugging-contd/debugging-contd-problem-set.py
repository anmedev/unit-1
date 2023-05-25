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

# Debugging Continued - id: 2404607e-9db0-48bd-9222-61a58913ffb4
# Moira's code produces this output: [SCREENSHOT OF ERROR]. What is the bug that Moira sees now? What is the expected output? What is the code doing?
# Answer: The bug in the code is causing every cell to evaluate to False, which means there are no living cells. The expected output is that the first generation should have three vertical living cells and the second generation should have three horizontal living cells. The code is setting every cell in the stage are evaluating to False.

# Debugging Continued - id: f9f85ba0-3390-46c0-9244-38b1bffa6821
# Moira wants to get her code working, but before she can do that she needs to understand why her code is doing what it's doing. Take a few minutes and use some debugging techniques to find out why her code is behaving the way it is. List a few of the things you tried and what you discovered.

# Answer: Add print statements inside the for loops to print the stage variable value.

# Debugging Continued - id: 882c916d-55ab-4c53-888b-8b8d68ea8021
# Why doesn't Moira's one_generation function work? Why are all of the cells dead in the second generation in the test?

# Answer: The code is changing the state of the cells before the neighbors are fully counted in the count_neighbors function.

# Debugging Continued - id: 4b1ba8ea-b9e5-4c37-b486-17fd865bc17b
# Moira knows what's happening and why it's happening. She's not quite sure yet how to fix her code, though! What are some debugging steps she can take as she works on a solution?

# Answer:
# Use print statements to get more information
# Use the Python Debugger
