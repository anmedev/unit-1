# Big O - id: b9HqKs
# What is the time complexity of the following piece of code? Assume that input_list is in sorted order.

def binary_search(input_list, value):
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if input_list[mid] > value:
            high = mid - 1
        elif input_list[mid] < value:
            low = mid + 1
        else:
            return mid

    if input_list[low] == value:
        return low

    return None

print(binary_search([1,2,3,4,5,6], 4))

# Answer: O(log n)