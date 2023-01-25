# Representing Data - ID: dZMTTi
def get_friend_data():
  animal_sightings = {"date": "2010-06-01", "location": "park", "crow_count": 3, "dog_count": 10, "cat_count" : 0, "pigeon_count" : 31}
  return animal_sightings
print(get_friend_data())

# Representing Data - ID: KkABtU
def sort_contestants_age_desc():
  names = ["Dane", "Neo", "Amara", "Mae", "Jules", "Brandi"]
  return names
print(sort_contestants_age_desc())

def get_my_preferences():
  data = {"name": "A.M.", "is_morning_person": True, "is_night_owl": False, "fav_song": None, "num_of_household_members": 4}
  return data
print(get_my_preferences())

# Representing Data - ID: mHGBgU
def add_preferences(preferences, category, value):
  preferences[category] = value
  return preferences
print(add_preferences({"name": "A.M.", "is_morning_person": True, "is_night_owl": False, "fav_song": None, "num_of_household_members": 4}, "age", 26))

# Representing Data - ID: 5LPH50
def add_grocery(grocery_list, new_item):
  grocery_list.append(new_item)
  return grocery_list
print(add_grocery(["eggs", "milk", "bread", "spinach", "broccoli"], "butter"))

# Representing Data - ID: LLU2tX

def copy_top_item(my_groceries, their_groceries):
  top_item = their_groceries[0]
  my_groceries[0] = top_item
  return my_groceries
print(copy_top_item(["eggs", "milk", "bread", "spinach", "broccoli", "butter"], ["chocolate", "ice cream", "bananas", "tomatoes", "chicken", "onion"]))