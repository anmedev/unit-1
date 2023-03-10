# Example: Dining Out
# Follow these steps for each example:
options = ["the place I'm craving but is too far away",
           "the place we always go to",
           "that place that just opened but looks too fancy"
           ]
for option in options:
    print(f"What about getting food from {option} tonight?")

# Read through the code and identify:
# 1a. What is the list?
# The list is called options

# 1b. What is each element?
# Each element represents the dining options a user can choose from. They include: "the place I'm craving but is too far away", "the place we always go to", and "that place that just opened but looks too fancy". All of these list elements are strings.

# 1c. What do we name each element?
# We name each element option

# 1d. How do we use each element in the loop?
# By iterating through each element and storing each element as a value in the option variable inside the print statement.

# 2. Predict what will print
# What about getting food from the place I'm craving but is too far away tonight?
# What about getting food from the place we always go to tonight?
# What about getting food from the place that just opened but looks too fancy tonight?

# 3. Run the code and check your prediction
# My prediction is correct.

# Example: Calculating Taxes
# Follow these steps for each example:
prices = [18.99, 56.00, 48.50, 18.50]

for price in prices:
    taxed_price = price * 1.101
    print(f"The cost of one item is {taxed_price}")

print("That sure was a meal!")

# Read through the code and identify:
# 1a. What is the list?
# The list is called prices.

# 1b. What is each element?
# Each element represents the meal prices that we will be calculating taxes for.

# 1c. What do we name each element?
# We name each element price

# 1d. How do we use each element in the loop?
# By iterating through each element and multiplying each element by 1.101, which is the tax amount. Each product will be stored in the taxed_price variable. The print statement will print the string and the new taxed price for each element. After the loop is complete, the print statement outside of the loop will print.

# 2. Predict what will print
# The cost of one item is 20.90799
# The cost of one item is 61.656
# The cost of one item is 53.3985
# The cost of one item is 20.3685
# That sure was a meal!

# 3. Run the code and check your prediction
# My prediction is correct.

# Building up a List of Results - Exercise
prices = [18.99, 56.00, 48.50, 18.50]
taxed_prices = []

for price in prices:
    taxed_price = price * 1.101
    taxed_prices.append(taxed_price)

print(taxed_prices)

# Is taxed_prices:

# 1. initialized as an empty array inside the for loop? Why or why not?
# It's initialized as an empty array outside the for loop. If it's done inside the loop, the taxed_prices array will update the replace the tax price for each element as the loop runs. When the final list is printed, instead of printing the tax price for each element, it will only print the tax price for the final element.

# 2. accessed or modified inside the for loop? How?
# It is modified inside the for loop by using the append function to add the updated tax price for each element to the tax_prices list.

# 3. accessed or modified after the for loop? How?
# It is accessed after the for loop by the print statement, which is using to print the final taxed_prices list after the loop is completed.

# Loop Review - id: e45acb1f-5be4-4f87-b6d2-60831f03d620
# Consider this code -- what does the variable language represent?

def display_most_spoken_languages():
    languages = ["Chinese", "Hindi", "English", "Spanish", "Arabic"]

    for language in languages:
        print(f"{language} is one of the top 5 most spoken languages in the world.")

    return languages

# Answer: A single element in the languages list. The value changes during iteration.