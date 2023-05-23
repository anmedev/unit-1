# Nested Data and Nested Loops - id: 8mavqk
# What is the syntax to get "6501 Island St. SE" from restaurants?
restaurants = [
    {
        "name": "Dough Zone",
        "cuisine": "Chinese",
        "address": "1299 Dough Ave N"
    },
    {
        "name": "Bingos",
        "cuisine": "Carribean",
        "address": "6501 Island St SE"
    },
    {
        "name": "Toyoda",
        "cuisine": "Japanese",
        "address": "12543 Sushi Way NE"
    }
]

# Answer: restaurants[1]["address"]

# Nested Data and Nested Loops - id: WfX3l1
# Implement get_restaurant_addresses(). This method takes in one parameter, restaurants. The method should return a list of restaurant addresses, which are strings.

restaurants = [
    {
        "name": "Dough Zone",
        "cuisine": "Chinese",
        "address": "1299 Dough Ave N"
    },
    {
        "name": "Bingos",
        "cuisine": "Carribean",
        "address": "6501 Island St SE"
    },
    {
        "name": "Toyoda",
        "cuisine": "Japanese",
        "address": "12543 Sushi Way NE"
    }
]

# Refactored Solution
def get_restaurant_addresses(restaurants):
    list_of_addresses = [restaurant["address"] for restaurant in restaurants]
    return list_of_addresses
print(get_restaurant_addresses(restaurants))

# Original Solution
# def get_restaurant_addresses(restaurants):
#     list_of_addresses = []
#     for dictionary in restaurants:
#       for key in dictionary:
#         if key == "address":
#           list_of_addresses.append(dictionary["address"])
#     return list_of_addresses
# print(get_restaurant_addresses(restaurants))

# Ada's Solution:
# def get_restaurant_addresses(restaurants):
#     addresses = []
#     for restaurant in restaurants:
#         addresses.append(restaurant["address"])
#     return addresses

# Nested Data and Nested Loops - id: 99WiYg
# What is the syntax to get "Lizzie" from students?

students = [
    ["Michelle", "Beyonce", "Kelly"],
    ["Luke", "Leia", "Han"],
    ["Gordon", "Lizzie", "Miranda"]
]

# Answer: students[2][1]

# Nested Data and Nested Loops - id: UOoCrY
# Implement get_student_names(). This method takes in one parameter, student_groups. The method should return a list of student names, which are strings.

students = [
    ["Michelle", "Beyonce", "Kelly"],
    ["Luke", "Leia", "Han"],
    ["Gordon", "Lizzie", "Miranda"]
]
def get_student_names(student_groups):


# Nested Data and Nested Loops - id: 613ccf11-e7e6-4fad-a1b1-6a962bcd8967
# What is the syntax to get "University of Washington" from schools?

schools = {
    "school 1": {
        "name": "Western Washington University",
        "city": "Bellingham"
    },
    "school 2": {
        "name": "University of Washington",
        "city": "Seattle"
    },
    "school 3": {
        "name": "Washington State University",
        "city": "Pullman"
    }
}

# Answer: schools["school 2"]["name"]

# Nested Data and Nested Loops - id: b54addb3-48b0-462a-9f6a-f9b749fba39f
# Implement get_school_names(). This method takes in one parameter, schools. The method should return a list of school names, which are strings.

def get_school_names(schools):
