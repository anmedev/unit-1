# Lists and References - id: 55890920-cfd1-47e0-96e8-4e2b1caa3ada
# True or False, a list variable directly references its elements.

# Answer: False

# Side Effects - id: f00befa4-e25a-40b6-b235-618bb0fca09a
# What is printed by this code segment?

def mystery(numbers):
    index = 0
    while index < len(numbers):
        numbers[index] *= 2
        index += 1
    
    return numbers

nums = [1, 2, 3, 4, 5]
mystery(nums)

print(nums[3])

# Answer: 8

# Time complexity of a function - id: 5a39abda-3557-49e7-bd9a-409dccc9e1a8
# What is the time complexity of the following function?

def max(numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Answer:

