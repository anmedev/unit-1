# For each example:

# 1. Identify the function call that leads to the error condition, and describe what about it is problematic
# 2. Identify what line of code inside the try-clause raises an error
# 3. Observe what happens during each except-clause

def is_valid_int(input_num):
    try:
        x = int(input_num)
    except ValueError as error:
        print(f"{error}. Please enter a valid number.")


is_valid_int("Clearly not a valid int")

# Answer:
# 1. The function call that leads to the error condition is is_valid_int("Clearly not a valid int"). The issue is that when the function is called, the string argument "Clearly not a valid int" is not a valid integer needed for the code to properly execute.
# 2. The line of code inside the try-clause that raises an error is line 9: x = int(input_num)
# 3. During the except-clause, the code confirms that the exception is a ValueError, the value stored in the error variable is raised, and the exception message is printed.

def enter_candy(candy_choice):
    candy_list = ["lollipops", "m&ms", "gummy bears"]
    try:
        print(f"Your candy choice is {candy_choice}")
        print(f"You selected {candy_list[candy_choice]}")
    except IndexError as error:
        print(f"A {error} was entered. Please enter 0, 1, or 2.")

enter_candy(9999)

# Answer:
# 1. The function call that leads to the error condition is enter_candy(9999). The issue is that when the function is called, the int value 999 is outside the index range of the candy_list. The first print statement in the try clause will execute but when the code encounters the second print statement, an exception will raise due to the index error.
# 2. The line of code inside the try-clause that raises an error is line 24: print(f"You selected {candy_list[candy_choice]}")
# 3. During the except-clause, the code confirms that the exception is an IndexError, the value stored in the error variable is raised, and the exception message is printed.

# Try-Except-Block - id: e45ab433-76f7-46b8-8203-92f7df1a7515
# Assume we have a function process_list which takes a list as an argument and performs an operation on it. If the function is passed something other than a list, it throws a TypeError exception. It may throw another type of exception if something else goes wrong.

# Re-order the following lines of code into a working try-except block. For this question, disregard proper indentation.

# Answer:
# 1. try:
# 2.    process_list(my_list)
# 3. except TypeError:
# 4.    print("Variable is not a list")
# 5. except:
# 6.    print("Something else went wrong")