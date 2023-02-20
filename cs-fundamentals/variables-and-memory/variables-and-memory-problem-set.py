# Variable Scope - id: 45bbfac6-3851-461a-9ef2-36832f43459d
# What is the value of result after the function is_letter_in_word is invoked as shown below?

def is_letter_in_word(word, letter):
  """
  input: word (string) and letter (single character)output: boolean
  """
  if letter not in word:
    result = False
  else:
    result = True
  return result
result = True
is_letter_in_word("hello", "x")

# Answer: True

# Variable Scope - id: b56446e2-22dc-47b3-901c-e3510dbbcbfb
# What is the value of result after the function is_letter_in_word is invoked as shown below?
def is_letter_in_word(word, letter):
  """
  input: word (string) and letter (single character)output: boolean
  """
  if letter not in word:
    result = False
  else:
    result = True

  return result

result = True
result = is_letter_in_word("hello", "x")

# Answer: False (the return value on line 32 overrides the global variable on line 31)

# Variables Are References - id: c8a41151-3eb4-4a4f-ac8d-cab3b1e869c3
# What are the values of a and b after the following code snippet is run?
a = "hello"
b = a
a = "world"
print(a)
print(b)
# a = "world", b = "hello"

# Variables are References - id: bf869b3d-23f9-4643-b1a4-9c661c865ac1
# What are the values of before_tax and after_tax after the following code snippet is run?
before_tax = 10
after_tax = before_tax  * 1.1
before_tax = 20
print(before_tax)
print(after_tax)

# before_tax = 20, after_tax = 11

# Variables Are References - id: 9c70af03-8c71-4995-8c02-46d32e6a2e10
# What are the values of all_stores and book_stores after the following code snippet is run?
all_stores = [
    {"name": "Ada's Technical Books", "type": "book"},
    {"name": "Elliott Bay", "type": "book"},
    {"name": "Central Co-op", "type": "grocery"}
]

book_stores = all_stores
book_stores.pop()
print(all_stores)
print(book_stores)

# Answer:
all_stores = [
    {"name": "Ada's Technical Books", "type": "book"},
    {"name": "Elliott Bay", "type": "book"},
]
book_stores = [
    {"name": "Ada's Technical Books", "type": "book"},
    {"name": "Elliott Bay", "type": "book"},
]

# Variables are References - id:  861b3fdf-8339-4031-897b-0e7f41f1c6ee
# What are the values of ada, elliott, and book_stores after the following code snippet is run?

ada = {"name": "Ada's Technical Books", "type": "book"}
elliott = {"name": "Elliott Bay", "type": "book"}

book_stores = [ada, elliott]

ada["city"] = "Seattle"
elliott["city"] = "Seattle"

print(ada)
print(elliott)
print(book_stores)

# Answer:
ada = {
    "name": "Ada's Technical Books",
    "type": "book",
    "city": "Seattle"
    }
elliot = {
    "name": "Elliott Bay",
    "type": "book",
    "city": "Seattle"
    }

book_stores = [
    {
        "name": "Ada's Technical Books",
        "type": "book",
        "city": "Seattle"
    },
    {
        "name": "Elliot Bay",
        "type": "book",
        "city": "Seattle"
    },
]