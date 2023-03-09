# Examples - Menu
# Follow these steps for each example:
menu = {
    "appetizer": "Brussels Sprouts",
    "beverage": "Fancy Lemonade"
}

for dish, food in menu.items():
    print(f"The special {dish} for tonight is the {food}.")

# Read through the code and identify:
# 1a. What is the dictionary
# The dictionary is called menu

# 1b. What is each key and value?
# The first key is "appetizer" and its corresponding value is "Brussel Sprouts". The second key is beverage" and its corresponding value is "Fancy Lemonade". The keys and values represent the menu items available.

# 1c. What do we name each key and value?
# We name each key dish and we name each value food.

# 1d. How do we use each key and value in the loop?
# By iterating over each key and its corresponding value and storing them in the dish and food variables respectively. As the loop runs, it will print the string along with the first key and value then it will print the same string with the second key and value.

# 2. Predict what will print
# The special appetizer for tonight is Brussel Sprouts.
# The special beverage for tonight is Fancy Lemonade.

# 3. Run the code and check your prediction
# My prediction is correct.

# Examples - Menu with Prices
# Follow these steps for each example:
menu = {
  "Brussels Sprouts": 18.99,
  "Fancy Lemonade": 56.00
}

for food, price in menu.items():
    taxed_price = price * 1.101
    print(f"The cost of {food} is {taxed_price}")

print("That sure was a meal!")

# Read through the code and identify:
# 1a. What is the dictionary
# The dictionary is called menu

# 1b. What is each key and value?
# The first key is "Brussel Sprouts" and its corresponding value is 18.99. The second key is "Fancy Lemonade" and its corresponding value is 56.00. The keys and values represent the menu items and their prices.

# 1c. What do we name each key and value?
# We name each key food and we name each value price.

# 1d. How do we use each key and value in the loop?
# By iterating over each key and its corresponding value and storing them in the dish and food variables respectively. The first value stored in the price variable will be  As the loop runs, it will print the string along with the first key and value then it will print the same string with the second key and value. After the loop is complete, the code will print the print statement outside of the loop.

# 2. Predict what will print
# The cost of Brussel Sprouts is 20.90799.
# The cost of Fancy Lemonade is 61.656.
# That sure was a meal!

# 3. Run the code and check your prediction
# My prediction is correct.