# Sets and Tuples - id: 7dd15f30-291b-4d04-9560-b041c0718279
def shopping_list(bruschetta, pesto_pasta, salsa):
  bruschetta_set = set(bruschetta)
  pesto_pasta_set = set(pesto_pasta)
  salsa_set = set(salsa)
  final_set = bruschetta_set | pesto_pasta_set | salsa_set
  final_set_list = list(final_set)
  return final_set_list
print(shopping_list(["bread", "olive oil", "garlic", "tomato", "basil", "balsamic vinegar", "salt"], ["pasta", "olive oil", "garlic", "basil", "parmesan", "pine nuts"], ["tomato", "onion", "garlic", "salt", "green onion", "cilantro", "jalapeno"]))
print(shopping_list([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]))