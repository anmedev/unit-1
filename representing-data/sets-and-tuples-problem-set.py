# Sets and Tuples - id: 7dd15f30-291b-4d04-9560-b041c0718279
def shopping_list(bruschetta, pesto_pasta, salsa):
  bruschetta_set = set(bruschetta)
  pesto_pasta_set = set(pesto_pasta)
  salsa_set = set(salsa)
  final_set = bruschetta_set | pesto_pasta_set | salsa_set
  return list(final_set)
print(shopping_list(["bread", "olive oil", "garlic", "tomato", "basil", "balsamic vinegar", "salt"], ["pasta", "olive oil", "garlic", "basil", "parmesan", "pine nuts"], ["tomato", "onion", "garlic", "salt", "green onion", "cilantro", "jalapeno"]))
print(shopping_list([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))

# Sets and Tuples - id: # Sets and Tuples - id: 5e945f7a-fa92-423e-8b55-6a1dd2b22f87
def make_insect_dex(bug_list):
  return set(bug_list)
print(make_insect_dex(["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]))
print(make_insect_dex(["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]))

# Sets and Tuples - id: 1df7dc4e-7858-470b-83c5-7e619a31cb18
def caught_only_by_first(first_list, second_list):
  first_list_set = set(first_list)
  second_list_set = set(second_list)
  return first_list_set - second_list_set
print(caught_only_by_first(["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"], ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]))
print(caught_only_by_first(["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"], ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]))

# Sets and Tuples - id: e7a154a4-1f4d-4c2c-bb04-b88d978f3aba
def caught_only_by_first(first_list, second_list):
  first_list_set = set(first_list)
  second_list_set = set(second_list)
  return first_list_set & second_list_set
print(caught_only_by_first(["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"], ["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"]))
print(caught_only_by_first(["stag beetle", "earwig", "millipede", "pill bug", "june bug", "lightning bug", "dragonfly"], ["lightning bug", "caterpillar", "ladybug", "lightning bug", "ladybug", "monarch butterfly", "june bug", "carpenter ant"]))