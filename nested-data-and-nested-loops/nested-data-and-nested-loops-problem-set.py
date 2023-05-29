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
    address_list = [restaurant["address"] for restaurant in restaurants]
    return address_list
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

student_groups = [
    ["Michelle", "Beyonce", "Kelly"],
    ["Luke", "Leia", "Han"],
    ["Gordon", "Lizzie", "Miranda"]
]

# Solution
def get_student_names(student_groups):
  student_names = [student for group in student_groups for student in group]
  return student_names
print(get_student_names(student_groups))

# Ada's Solution
# def get_student_names(student_groups):
#     names = []
#     for group in student_groups:
#         for student in group:
#             names.append(student)
#     return names

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

# Solution
def get_school_names(schools):
  school_names = [schools[school]["name"] for school in schools]
  return school_names
print(get_school_names(schools))

# Ada's First Solution:
# def get_school_names(schools):
#     names = []
#     for school_num in schools:
#         names.append(schools[school_num]["name"])
#     return names

# Ada's Second Solution:
# def get_school_names(schools):
#     names = []
#     for school_num, school in schools.items():
#         names.append(school["name"])
#     return names

# Nested Data and Nested Loops - id: Q9vx6M
# It's karaoke night! What is the syntax to get "Jolene" from karaoke_queue?

karaoke_queue = {
  "Rajan": ["I Want It That Way", "Jolene"],
  "Akira": ["Return of the Mack", "Mr. Brightside"],
  "Linh": ["Say My Name", "Since You Been Gone"]
}
# Answer: karaoke_queue["Rajan"][1]

# Nested Data and Nested Loops - id: 1VNr86
# It's karaoke night! Implement get_song_list(). This method takes in one parameter, karaoke_queue. The method should return a list of song titles, which are strings.

karaoke_queue = {
  "Rajan": ["I Want It That Way", "Jolene"],
  "Akira": ["Return of the Mack", "Mr. Brightside"],
  "Linh": ["Say My Name", "Since You Been Gone"]
}

# Refactored Solution:
def get_song_list(karaoke_queue):
  song_list = [song for song_titles in karaoke_queue.values() for song in song_titles]
  return song_list
print(get_song_list(karaoke_queue))

# Original Solution:
# def get_song_list(karaoke_queue):
#     song_list = []
#     for song_titles in karaoke_queue.values():
#         for song in song_titles:
#             song_list.append(song)
#     return song_list
# print(get_song_list(karaoke_queue))

# Ada's Solution:
# def get_song_list(karaoke_queue):
#     song_list = []
#     for performer, performer_queue in karaoke_queue.items():
#         for song in performer_queue:
#             song_list.append(song)
#     return song_list
