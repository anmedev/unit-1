# Nested Loops - id: sF6pz1
# How many loops are in the function map_character_frequency() ?
def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map:
                char_map[character] = 1
            else:
                char_map[character] += 1
    return char_map

colors = ["red", "orange", "yellow", "green"]

colors_char_map = map_character_frequency(colors)
print(colors_char_map)

# Answer: 2 for-loops, 0 while-loops

# Nested Loops - id: 9fw2wh
# Which line of code best describes iterating over the list words ?

# Answer: for word in words:

# Nested Loops - id: myW4kq
# What is the local variable for each item in words ?

# Answer: word

# Nested Loops - id: hAerR2
# Which line of code best describes iterating over each character in word ?

# Answer: for character in word:

# Nested Loops - id: 9ShXFW
# What is the local variable for each item in word?

# Answer: character