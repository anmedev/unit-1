# Problem Statements and Functions - id: 7eaadcae-9001-4d2f-a6e6-3242e28ac4f1
# Imagine that you maintain a lot of plants. For any given plant, you need to check if it needs water, check if it needs sunlight, and a few other tasks. You're creating one function to describe all of those tasks. Which of these is the best name for this function?

# Answer: maintain_plant(plant)

# Problem Statements and Functions - id: ooI7dJ
# You are writing a function named needs_water, which will return whether or not a plant needs water. What data type is this needs_water most likely going to return?

# Answer: Boolean

# Problem Statements and Functions - id: EPPL9w
# You are writing a function named relocate_plant, which will take one plant and a proposed new spot for it, and move the plant there. Which one of these is the best set of parameters?

# Answer: relocate_plant(plant, location)

# Syntax - id: v6k6kC
# Given this code...identify this piece of syntax: def maintain_plant(plant):

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: Function Signature

# Syntax - id: 8TrnuR
# Given this code (duplicated from above)...specifically in the line def maintain_plant(plant):, identify this piece of syntax: plant

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: Parameter

# Syntax - id: owr3gL
# Given this code (duplicated from above)...specifically in the line def maintain_plant(plant):, identify this piece of syntax: maintain_plant

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: Function name

# Syntax - id: owr3gL
# Given this code (duplicated from above)...identify this piece of syntax: relocate(plant, new_location)

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: Function call

# Syntax - id: owr3gL
# Given this code (duplicated from above)...identify this piece of syntax: "A Mellow Mood for Maidenhair"

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: Argument

# Syntax - id: 43ENx4
# Given this code (duplicated from above)...pick the best description for what this code is doing: new_location = find_available_sunny_spot(plant)

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: new_location is set to the value that find_available_sunny_spot(plant) evaluates to

# Syntax - id: y2O2w2
# Given this code (duplicated from above)...pick the best description for what this code is doing: return plant

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: Returns the value assigned to the variable plant

# Syntax - id: y2O2w2
# Given this code (duplicated from above)...pick the best description for what this code is doing: 
# if needs_water(plant):
#     water(plant)

# def maintain_plant(plant):
#     if needs_water(plant):
#         water(plant)
#     if needs_sunlight(plant):
#         new_location = find_available_sunny_spot(plant)
#         relocate(plant, new_location)
#     sing_to_plant(plant, "A Mellow Mood for Maidenhair")
#     return plant

# Answer: If the function call needs_water(plant) is True, then call the function water() with the argument plant

# Syntax Reordering - id: Fr02Z
# Reorder the lines of code below to create a function that assembles the lyrics of the song "I'm a Little Teapot." If multiple arrangements would generate the same result, be sure to pick the least surprising arrangement. Assume that each line would be indented correctly. The song lyrics are, "I'm a little teapot, Short and stout. Here is my handle, Here is my spout!"
def sing_teapot_song():
  first_line = "I'm a little teapot,"
  second_line = "Short and stout."
  third_line = "Here is my handle,"
  fourth_line = "Here is my spout!"
  full_song = f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}"
  return full_song
print(sing_teapot_song())

# Reading Code - id: 2rhUAe
# Read through this code. Assume that get_season() and get_day_of_week() are valid functions. What does this function do?
# def get_daily_special(todays_date):
#     current_season = get_season(todays_date)

#     if current_season == "Spring":
#         special = "Eggplants"
#     elif current_season == "Summer":
#         special = "Blueberries"
#     elif current_season == "Fall":
#         special = "Sweet Potatoes"
#     else:
#         special = "Oranges"

#     day_of_week = get_day_of_week(todays_date)

#     if day_of_week == "Saturday" or day_of_week == "Sunday":
#         special = f"Weekend {special}"

#     return special

# Answer: Determines the special based on today's season and day of the week

# Debugging Functions - id: Rxvbnm
# Assuming that get_season() and get_day_of_week() are valid functions, given this code...there is a syntax or runtime error in this code. What is the cause of this error?
# def get_daily_special(todays_date):
# current_season = get_season(todays_date)

#     if current_season == "Spring":
#         special = "Eggplants"
#     elif current_season == "Summer":
#         special = "Blueberres"
#     elif current_season == "Fall":
#         special = "Sweet Potatoes"
#     else:
#         special = "Oranges"

#     day_of_week = get_day_of_week(todays_date)

#     if day_of_week == "Saturday" or day_of_week == "Sunday":
#         special = f"Weekend {special}"

#     return special

# Answer: Incorrect indentation

# Debugging Functions - id: uS0vJj
# Assuming that get_season() and get_day_of_week() are valid functions, given this code...there is a syntax or runtime error in this code. What is the cause of this error?
# def get_daily_special(todays_date):
# current_season = get_season(todays_date)

#     if current_season == "Spring":
#         special = "Eggplants"
#     elif current_season == "Summer":
#         special = "Blueberres"
#     elif current_season == "Fall":
#         special = "Sweet Potatoes"
#     else:
#         special = "Oranges"

#     day_of_week = get_day_of_week(todays_date)

#     if day_of_week == "Saturday" or day_of_week == "Sunday":
#         special = f"Weekend {special}"

#     return special

# Answer: Missing colon (else statement)

# Debugging Functions - id: T2IbR3
# Assuming that get_season() and get_day_of_week() are valid functions, given this code...there is a syntax or runtime error in this code. What is the cause of this error?
# def get_daily_special(todays_date):
#     current_season = get_season(todays_date)

#     if current_season == "Spring":
#         special = "Eggplants"
#     elif current_season == "Summer":
#         special = "Blueberries"
#     elif current_season == "Fall":
#         special = "Sweet Potatos"
#     else:
#         special = "Oranges"

#     get_day_of_week(todays_date)

#     if day_of_week == "Saturay" or day_of_week == "Sunday":
#         special = f"Weekend {special}"

#     return special

# Answer: Reads a variable that has no value

# Debugging Functions - id: XpTwkZ
# Assuming that get_season() and get_day_of_week() are valid functions, given this code...there is a syntax or runtime error in this code. What is the cause of this error?
# def get_daily_special(todays_date):
#     current_season = get_season(todays_date)

#     if current_season == "Spring":
#         special = "Eggplants"
#     elif current_season == "Summer":
#         special = "Blueberries"
#     elif current_season == "Fall":
#         special = "Sweet Potatoes"
#     else:
#         specail = "Oranges"

#     day_of_week = get_day_of_week(todays_date)

#     if day_of_week == "Saturday" or day_of_week == "Sunday":
#         specail = f"Weekend {special}"

#     return special

# Answer: Misspelling (specail)

# Adding to Existing Functions - id: CUhJy2
# Following the current pattern in the code below, modify the function so that invoking get_example_sentence("they/them") returns "They went to the park. I went with them. They brought their frisbee.", and doesn't alter the rest of the functionality.
def get_example_sentence(pronouns):
    if pronouns == "she/her":
      return "She went to the park. I went with her. She brought her frisbee."
    elif pronouns == "he/him":
      return "He went to the park. I went with him. He brought his frisbee."
    elif pronouns == "they/them":
      return "They went to the park. I went with them. They brought their frisbee."
    elif pronouns == "ze/hir":
      return "Ze went to the park. I went with hir. Ze brought hir frisbee."
    else:
      return "I'm not quite sure how to use these pronouns, it's best to ask and confirm!"
print(get_example_sentence("they/them"))
