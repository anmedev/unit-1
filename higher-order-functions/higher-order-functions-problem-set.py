# Higher Order Functions - id: 2a948f45-615e-4e79-8f90-260bd231ba28
# Check all the example function calls that represent valid syntax.

# Answer: a| c| d| e| f|
# a| function_name(argument1, argument2)
# c| function_name(parameter1=argument1, parameter2=argument2)
# d| function_name(argument1, parameter2=argument2)
# e| function_name(argument1, parameter2=argument2, parameter3=argument3)
# f| function_name(argument1, argument2, parameter3=argument3)

# Higher Order Functions - id: 7bbe5762-40e2-40f3-8af5-b6d3786ea57d
# Imagine you have a list of dictionaries that represents the words and their score in the Adagrams game. Write a function get_max_word that takes a list of word dictionaries. You should use the max function with the key parameter such that the get_max_word function returns the word dictionary with the highest score.

# You should also write a named function get_score that is passed to the key parameter. In the next code challenge, you will be asked to use a lambda expression.

# In the case of a tie, the function should return the first element it sees. In the case of an empty list, it should return None.

# Solution
def get_score(word):
  return word["score"]

def get_max_word(words):
    if not words:
      return None
    max_word = max(words, key = get_score)
    return max_word
print(get_max_word([{"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "are", "score": 3}, {"word": "you", "score": 6}])) # {"word": "how", "score": 9}
print(get_max_word([{"word": "ada", "score": 4}, {"word": "roar", "score": 4}])) # {"word": "ada", "score": 4}
print(get_max_word([{"word": "how", "score": 9}])) # {"word": "how", "score": 9}
print(get_max_word([])) # None

# Higher Order Functions - id: f1b9b711-4a92-4612-9147-7e305cd89c17
# Imagine you have a list of dictionaries that represents the words and their score in the Adagrams game. Write a function get_max_word that takes a list of word dictionaries. You should use the max function with the key parameter such that the get_max_word function returns the word dictionary with the highest score.

# Your solution should use a lambda expression.

# In the case of a tie, the function should return the first element it sees. In the case of an empty list, it should return None.

# Solution
def get_max_word(words):
    if not words:
      return None
    max_word = max(words, key = lambda word: word["score"])
    return max_word
print(get_max_word([{"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "are", "score": 3}, {"word": "you", "score": 6}])) # {"word": "how", "score": 9}
print(get_max_word([{"word": "ada", "score": 4}, {"word": "roar", "score": 4}])) # {"word": "ada", "score": 4}
print(get_max_word([{"word": "how", "score": 9}])) # {"word": "how", "score": 9}
print(get_max_word([])) # None

# Higher Order Functions - id: 36789c28-3e3c-4d4e-9a4c-456cd1cd691d
# Imagine you have a list of dictionaries that represents the words and their score in the Adagrams game. Write a function sort_words that takes a list of word dictionaries. You should use the sorted function with the key parameter such that the sort_words function returns a list of word dictionaries sorted alphabetically by "word".

# Solution
def sort_words(words):
    sorted_words = sorted(words, key = lambda word: word["word"])
    return sorted_words
print(sort_words([{"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "are", "score": 3}, {"word": "you", "score": 6}])) # [{"word": "are", "score": 3}, {"word": "hi", "score": 5}, {"word": "how", "score": 9}, {"word": "you", "score": 6}]
print(sort_words([{"word": "roar", "score": 4}, {"word": "ada", "score": 4}])) # [{"word": "ada", "score": 4}, {"word": "roar", "score": 4}]
print(sort_words([{"word": "how", "score": 9}])) # [{"word": "how", "score": 9}]
print(sort_words([])) # []

