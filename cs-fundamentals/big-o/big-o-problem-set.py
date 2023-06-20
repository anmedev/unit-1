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