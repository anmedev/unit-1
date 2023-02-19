# Variable Scope - id: 45954838-a89d-4b65-a5db-e6e52aae3ed7
# Finish this sentence: Variable scope is...
# Answer: the area of a program where a variable can be accessed

# Local Variables - id: e3584e35-5c7d-4e46-a210-a1a0b697e8c0
# Read this code, and assume cut, cook, and plate are all valid, defined functions. Variables that can be read inside of the prepare_dinner function are...

# def prepare_dinner(ingredients):
#     chopped_food = cut(ingredients)
#     cooked_food = cook(chopped_food)
#     plated_food = plate(cooked_food)
#     return plated_food

# prepare_dinner(["Jackfruit", "Onion", "Mango", "Avocado", "Ginger", "Cucumber", "Lime", "Jalapeño"])

# Answer: ingredients, chopped_food, cooked_food, plated_food

# Describe These Variables
# Read this code, and assume cut, cook, and plate are all valid, defined functions. Which of these describe the variables (and their scope) inside of this code?

# def prepare_dinner(ingredients):
#     chopped_food = cut(ingredients)
#     cooked_food = cook(chopped_food)
#     plated_food = plate(cooked_food)
#     return plated_food

# dinner_recipe = ["Jackfruit", "Onion", "Mango", "Avocado", "Ginger", "Cucumber", "Lime", "Jalapeño"]
# prepare_dinner(dinner_recipe)

# Answer: dinner_recipe is a global variable. ingredients is a parameter. chopped_food, cooked_food, and plated_food are local variables. They can all be accessed inside of the function.
