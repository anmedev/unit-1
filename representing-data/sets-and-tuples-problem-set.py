# Sets and Tuples - id: 7dd15f30-291b-4d04-9560-b041c0718279
bruschetta = ["bread", "olive oil", "garlic", "tomato", "basil", "balsamic vinegar", "salt"]
pesto_pasta = ["pasta", "olive oil", "garlic", "basil", "parmesan", "pine nuts"]
salsa = ["tomato", "onion", "garlic", "salt", "green onion", "cilantro", "jalapeno"]
def shopping_list(bruschetta, pesto_pasta, salsa):
  bruschetta_set = set(bruschetta)
  pesto_pasta_set = set(pesto_pasta)
  salsa_set = set(salsa)
  final_set = bruschetta_set | pesto_pasta_set | salsa_set
  return list(final_set)
print(shopping_list(bruschetta, pesto_pasta, salsa))

# Sets and Tuples - id: 5e945f7a-fa92-423e-8b55-6a1dd2b22f87
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
def make_insect_dex(bug_list):
  return set(bug_list)
print(make_insect_dex(mady_bugs))
print(make_insect_dex(lesha_bugs))

# Sets and Tuples - id: 1df7dc4e-7858-470b-83c5-7e619a31cb18
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
def caught_only_by_first(first_list, second_list):
  first_list_set = set(first_list)
  second_list_set = set(second_list)
  return first_list_set - second_list_set
print(caught_only_by_first(mady_bugs, lesha_bugs))
print(caught_only_by_first(lesha_bugs, mady_bugs))

# Sets and Tuples - id: e7a154a4-1f4d-4c2c-bb04-b88d978f3aba
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
def caught_by_both(first_list, second_list):
  first_list_set = set(first_list)
  second_list_set = set(second_list)
  return first_list_set & second_list_set
print(caught_by_both(mady_bugs, lesha_bugs))
print(caught_by_both(lesha_bugs, mady_bugs))

# Sets and Tuples - id: c43f2ad4-b5b4-428b-8899-438decd86d2f
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
def caught_together(first_list, second_list):
  first_list_set = set(first_list)
  second_list_set = set(second_list)
  return first_list_set | second_list_set
print(caught_together(mady_bugs, lesha_bugs))
print(caught_together(lesha_bugs, mady_bugs))

# Sets and Tuples - id:  3b751423-f9d1-41b6-852d-6735e457bd0f
mady_bugs = ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]
lesha_bugs = ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]
journal_bugs = ["pill bug", "damselfly", "stag beetle", "ladybug", "honey bee", "monarch butterfly", "moth", "caterpillar", "earwig", "lightning bug", "dragonfly", "stag beetle", "millipede", "june bug", "carpenter ant"]
def left_to_catch(bug_list, journal_bugs_list):
  bug_list_set = set(bug_list)
  journal_bugs_set = set(journal_bugs_list)
  return journal_bugs_set - bug_list_set
print(left_to_catch(mady_bugs, journal_bugs))
print(left_to_catch(lesha_bugs, journal_bugs))

# Sets and Tuples - id: 8847d1ad-0ce1-43db-aa82-33f9f744aecb
carmelo_sequences = {
    (1, 2, 3, 4, 5, 6, 7, 8),
    (2, 4, 6, 8, 10, 12, 14, 16),
    (1, 1, 2, 3, 5, 8, 13, 21),
    (1, 3, 6, 10, 15, 21, 28, 36),
}
fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
def is_known_sequence(sequence, known_sequences):
  sequence = tuple(sequence)
  if sequence in known_sequences:
    return True
  return False
print(is_known_sequence(fibonacci_sequence, carmelo_sequences))
print(is_known_sequence(prime_numbers, carmelo_sequences))

# Sets and Tuples - id:  76b680cf-c278-44ca-bdda-146c3c3866ea
fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21]
positive_even_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
triangular_numbers = [1, 3, 6, 10, 15, 21, 28, 36]

def get_first_and_last(sequence):
  first = sequence[0]
  last = sequence[-1]
  return first, last
first, last = get_first_and_last(fibonacci_sequence)
print((first, last))
first, last = get_first_and_last(positive_even_numbers)
print((first, last))
first, last = get_first_and_last(prime_numbers)
print((first, last))
first, last = get_first_and_last(triangular_numbers)
print((first, last))

# Sets and Tuples - id: 2a510580-ed13-4150-b591-0619d4b0ab74
product_table = {}
def store_product_of_pairs(product_table, first, last):
  product_table[(first, last)] = first * last
  return first * last
print(store_product_of_pairs(product_table, 1, 21))
print(store_product_of_pairs(product_table, 2, 16))
print(store_product_of_pairs(product_table, 2, 19))
print(store_product_of_pairs(product_table, 1, 36))
print(product_table)