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

# Answer: O(n) - Linear

# Space complexity of a function - id: 5bbb9400-054c-4667-a82c-86d5b3642e2b
# What is the space complexity of the following function?

def max(numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Answer: O(1) - Constant

# Space Complexity Question 2 - id: 727f7ca4-61e8-418d-803f-106c1841367a
# What is the space complexity of the following function?

def long_words(words):
    big_words = []
    for word in words:
        if len(word) > 5:
            big_words.append(word)
    return big_words

# Answer: O(n)

# Sorting Algorithms - id: fN9PLJ
# Describe the algorithm for Insertion Sort in your own words. Make sure to touch on:

# What makes this different from other algorithms we've seen?
# What is its time and space complexity?
# What factors contribute to its time complexity?
# Answer in 3-6 sentences, draw a picture and describe it, or write a poem, an analogy, or a story.

# Answer: Insertion sort algorithm splits a list into a sorted and unsorted side. Each item in the unsorted side is then put in its proper place on the sorted side of the list. Insertion sort has a quadratic time complexity and a constant space complexity. The factors that contribute to its time complexity include the number of comparisons performed in the inner loop.
