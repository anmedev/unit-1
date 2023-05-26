# Exception Handling - id: XwJz6l
# Given these tests, provide the function body that will make them pass. Assume that the only invalid, claimed code school name is "Ada Developers Academy".

# Tests
# def test_valid_name():
#     result = claim_unreserved_code_school_name("Some Code School")
#     assert result is True


# def test_invalid_name():
#     with pytest.raises(ValueError):
#         claim_unreserved_code_school_name("Ada Developers Academy")

# Solution:
def claim_unreserved_code_school_name(name):
    if name == "Ada Developers Academy":
        raise ValueError
    return True

# Exception Handling - id: SkMsOl
# Given these tests, provide the function body that will make them pass. Assume that any phone number that is a string is valid. Hint: The function type(phone_num) will return str if phone_num is a string.

# Tests
# def test_valid_phone_nums_return_true():
#     phone_num = "777-888-9999"
#     is_valid = is_phone_num_valid(phone_num)
#     assert is_valid

# def test_invalid_phone_nums_raise_error():
#     phone_num = 777-888-9999
#     with pytest.raises(TypeError):
#         is_valid = is_phone_num_valid(phone_num)

# Solution
def is_phone_num_valid(phone_num):
    if type(phone_num) is not str:
        raise TypeError
    return True

# Exception Handling - id: VLwvhu
# Given these tests, refactor this function to make them pass. Use try ... except syntax.

# If no error is raised, return cost_per_person
# If a ZeroDivisionError is raised, catch it, and return 0

# Tests
# def test_split_cost_evenly():
#     cost = split_cost_evenly(100, 4, .5)
#     assert cost == pytest.approx(37.5)

# def test_caught_zerodivisionerror_returns_zero():
#     cost = split_cost_evenly(100, 0, .5)
#     assert cost == 0

# Solution:
def split_cost_evenly(total_cost, num_of_people, tip_percentage):
    try:
      cost_with_tip = total_cost * (1 + tip_percentage)
      cost_per_person = cost_with_tip / num_of_people
      return cost_per_person
    except ZeroDivisionError:
        return 0

# Exception Handling - id: j9kUX9
# Given these tests, refactor only the get_celebration_treat function to make them pass. Use try ... except syntax. In get_celebration_treat...

# If no error is raised, then get_celebration_treat returns "celebration {thirteenth_donut}!", where thirteenth_donut is the result of grab_thirteenth_donut()
# If an IndexError is raised because of accessing something missing in donuts, then get_celebration_treat returns "no donut :("

# Tests
# def test_get_celebration_treat():
#     bakers_dozen = [
#         "glazed donut", "old-fashioned", "jelly donut", "bear claw", "classic donut with pink frosting and sprinkles on top", "donut hole", "another glazed donut", "yet another glazed donut?", "cruller", "maple donut", "powdered sugar donut", "doughnut", "thirteenth donut"
#     ]
#     # Run this assert as part of the "Arrange" step to ensure we're set up correctly
#     assert len(bakers_dozen) == 13

#     thirteenth_donut = get_celebration_treat(bakers_dozen)
#     assert thirteenth_donut == "celebration thirteenth donut!"

# def test_no_celebration_treat():
#     empty_donut_box = []
#     # Run this assert as part of the "Arrange" step to ensure we're set up correctly
#     assert len(empty_donut_box) != 13

#     no_donut = get_celebration_treat(empty_donut_box)
#     assert no_donut == "no donut :("

# def test_dont_grab_thirteenth_donut():
#     # This test is for checking that grab_thirteenth_donut raises the error
#     empty_donut_box = []
#     with pytest.raises(IndexError):
#         grab_thirteenth_donut(empty_donut_box)

# Solution:
def grab_thirteenth_donut(donuts):
    return donuts[12]

def get_celebration_treat(treats):
    try:
      thirteenth_donut = grab_thirteenth_donut(treats)
      return f"celebration {thirteenth_donut}!"
    except IndexError:
        return f"no donut :("

# Exception Handing - id: UlAHwy
# Given these tests, refactor only the prepare_meal function to make them pass. Use try ... except syntax. In prepare_meal...

# If no error is raised, then food should be the result of make_breakfast(pantry)
# If a KeyError is raised because of accessing something missing in pantry, then food should be "nothing"

# Tests
# def test_makes_breakfast_on_a_plate():
#     pantry = {
#         "waffles": "blueberry waffles",
#         "juice": "orange juice"
#     }
#     breakfast = prepare_meal("breakfast", pantry)
#     assert breakfast == "blueberry waffles and orange juice on a plate!"

# def test_missing_pantry_items_gets_nothing_on_a_plate():
#     empty_pantry = {}
#     missing_breakfast = prepare_meal("breakfast", empty_pantry)
#     assert missing_breakfast == "nothing on a plate!"

# def test_make_breakfast_with_empty_pantry():
#     # This test is for checking that make_breakfast raises the error
#     empty_pantry = {}
#     with pytest.raises(KeyError):
#         make_breakfast(empty_pantry)

# Solution:
def make_breakfast(pantry):
    breakfast = f"{pantry['waffles']} and {pantry['juice']}"
    return breakfast

def serve_food(food):
    return food + " on a plate!"

def prepare_meal(meal_type, pantry):
    try:
      if meal_type == "breakfast":
        food = make_breakfast(pantry)
    except KeyError:
        food = "nothing"
    meal = serve_food(food)
    return meal