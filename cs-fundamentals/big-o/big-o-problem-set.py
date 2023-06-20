# Big O - id: rhpVnF
# What is the time complexity of the following piece of code?

def does_value_exist(input_list, value):
    for item in input_list:
        if item == value:
            return True
    return False

# Answer: O(n) - linear
# Ada's Explanation: The provided code linearly searches through each item in the list to check if the value is found. In the worst case scenario, all items in the list are searched. This means if there are n items in the list, all n items will be checked. In the best case scenario, the value to be found would be the first item in the list. In the average case, the number of times the loop will run will be somewhere in between the best case and worst case, but still dependent on the number of items in the list, i.e. n. The time complexity of this algorithm is therefore linear or O(n) where n is the length of the input_list.

# Big O - id: fFOaNl
# What is the time complexity of the following piece of code?

def repeat_four_times(value):
    for count in range(4):
        print("The value is", value)

# Answer: O(1) - Constant
# Ada's Explanation: Independent of the input parameter value, the loop in this method will always run four times. Because the number of iterations in the loop is constant and independent of input parameter size or value, the time complexity will be constant or O(1).

# Big O - id: 2sHTBq
# What is the time complexity of the following piece of code?

def repeat_multiple_times(value, num_of_repetitions):
    for count in range(num_of_repetitions):
        print("The value is", value)

# Answer: O(n) - Linear
# Ada's Explanation: This method executes the print instruction num_of_repetitions times. If the value of num_of_repetitions changes, the number of times the print instruction is repeated will change linearly. Therefore, the time complexity of this algorithm is linear or O(n) where n is the supplied number of repetitions.

# Big O - id: BAKq4K
# What is the time complexity of the following piece of code?

def greet_friends(input_list):
    for num in range(len(input_list)):
        print(f"Hello, Friend #{num + 1}!")

# Answer: O(n) - Linear
# Ada's Explanation: This method will execute the print statement as many times as is the length of the input_list. If the size of the input_list changes, the number of times the print statement gets executed will change to match the size. Since the number of times the print statement gets executed is linearly proportional to the length of the input_list, the time complexity is linear or O(n) where n is the length of the input_list.

# Big O - id: SULbFB
# What is the time complexity of the following piece of code?

def greet_friends(input_list):
    i = 0
    while i < 17:
        print(f"Hello, Friend #{i + 1}!")
        i += 1

# Answer: O(1) - Constant
# Ada's Explanation: The loop in this method gets run 17 times regardless of the size or value of the input list. Hence, the time complexity of constant or O(1).

# Big O - id: 4w506R
# What is the time complexity of the following piece of code?

def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < count:
        print(f"Hello, Friend #{i + 1}!")
        i += 1

# Answer: O(n) - Linear
# Ada's Explanation: The loop in this method gets run count times. count is the length of input_list. As the length of input_list changes, so will the number of times the loop gets executed. The execution of the loop is linearly proportional to the length of input_list. So, the time complexity is linear or O(n) where n is the length of the input parameter, input_list.

# Big O - id: bfvZeu
# What is the time complexity of the following piece of code?

def greet_friends(input_list):
    count = len(input_list)
    i = 0
    while i < count:
        for j in range(count):
            print(f"Hello, Friend #{i+1} in {j+1}!")
        i += 1

# Answer: O(n2) - Quadratic
# Ada's Explanation: There are two nested loops in this method. Each loop runs n times where n is the length of input_list. Since the loops are nested, the loop will run n * n times. So, the time complexity of this algorithm is O(n2) where n is the length of the input input_list. In other words, the time complexity is quadratic, which is a polynomial time complexity.

# Big O - id: rkV75c
# What is the time complexity of the following piece of code?

def greet_friends(input_list):
    count = len(input_list)
    k = 0
    while k != count:
        i = 0
        while i < count:
            for j in range(count):
                print(f"Hello, Friend #{i+1} in #{j+1}!")
            i += 1
        k += 1

# Answer: O(n3) - Cubic
# Ada's Explanation: There are three nested loops in this method, each running n times where n is the length of input_list. The time complexity will therefore be n * n * n or in Big O terms O(n3). In other words, the time complexity will be cubic, which is a polynomial time complexity.