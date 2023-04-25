# Nested Lists and Dictionaries - id: c49169ab-1a7c-447b-9399-4ee331e5d596
# Use 1-4 sentences to describe this data structure. Describe each layer of the data structure, starting with the outer data structure.

clothes = [
  ["hat", "beanie", "fedora"],
  ["tshirt", "hoodie", "cardigan"],
  ["jeans", "joggers", "shorts"]
]

# Answer: This data structure is a two-dimensional array, or a list of lists. It has an outer list called clothes and inside this clothes list are three inner lists. These three inner lists all have the same length of 3 elements.

# Nested Lists and Dictionaries - id: e4927780-c756-4b5d-9cbe-acdfa0859d1f
# Use 1-4 sentences to describe this data structure. Describe each layer of the data structure, starting with the outer data structure.
sandwich = {
  "blt": ["bacon", "lettuce", "tomato"],
  "grilled cheese": ["american cheese", "gruyere"],
  "pbj": ["grape jelly", "peanut butter"]
}

# Answer: This data structure is a dictionary of lists. It has an outer dictionary called sandwiches and inside this sandwiches dictionary, are three inner lists. These lists are called "blt", "grilled cheese", and "pbj" respectively and they have varying list lengths.

# Nested Lists and Dictionaries - id: gKsPNt
# What is the syntax to get 25 from pokedex?
pokedex = [
        {
            "id": 25,
            "name_en": "Pikachu",
            "type": "Electric"
        }
    ]

# Answer: pokedex[0]["id"]

# Nested Lists and Dictionaries - id: yqGKmA
pokedex = [
        {
            "id": 25,
            "name_en": "Pikachu",
            "type": "Electric"
        }
    ]

# Answer: pokedex[0]["type"]

# Nested Lists and Dictionaries - id: wfpvr0
# Let's practice with a nested data structure that is three layers deep! What is the syntax to get "Pikachu" from game_data?

game_data = {
    "pokedex": [
        {
            "id": 25,
            "name_en": "Pikachu",
            "type": "Electric"
        }
    ]
}
# Answer: game_data["pokedex"][0]["name_en"]

# Nested Lists and Dictionaries - id:  1gcwNk
# What is the syntax to get [{"id": 25, "name_en": "Pikachu", "type": "Electric"}] from game_data?

game_data = {
    "pokedex": [
        {
            "id": 25,
            "name_en": "Pikachu",
            "type": "Electric"
        }
    ]
}

# Answer: game_data["pokedex"]

# Nested Lists and Dictionaries - id: mXiwq8
# What is the syntax to get {"id": 25, "name_en": "Pikachu", "type": "Electric"} from game_data?

game_data = {
    "pokedex": [
        {
            "id": 25,
            "name_en": "Pikachu",
            "type": "Electric"
        }
    ]
}
# Answer: game_data[pokedex][0]
