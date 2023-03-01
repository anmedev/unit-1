# Identifying Test Cases - id: 6cc1f1e5-b54a-4d89-900f-2d18f8db240d
# Complete Part 1 outlined in the README of the tdd-exercise replit. Record your test cases below.

# Answer:

# Intro to Pytest - id: oLlaji
# We want to test calculate() and verify that when either num_a or num_b aren't integers or floats, the function returns "Type Error: num_a and num_b must be integer or float". Which of these is the best name for a test?
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"

    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"

# Answer: test_calculate_non_numbers_returns_type_error()

# Intro to Pytest - id: jPjWs2
# We want to test calculate() and verify the case when it returns "Value Error: Operator Not Found". Which of these is the best name for a test?
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"

# Answer: test_calculate_invalid_operator_returns_error_msg()

# Intro to Pytest - id: OKElap
# We want to test calculate() and verify that multiplying two numbers works successfully. Which of these is the best name for a test?
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"

# Answer: test_calculate_multiplies_two_numbers()

# Intro to Pytest - id: v09uFR
# We want to test calculate() and verify the case when it returns "Zero Division Error". Which of these is the best name for a test?
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"

# Answer: test_calculate_dividing_by_zero_returns_error_msg()

# Intro to Pytest - id: KlpcjW
# Consider calculate(). Which of these are valid test cases to have assertions for?
def calculate(num_a, num_b, operator):
    if not (
        (isinstance(num_a, int) or isinstance(num_a, float)) and
            (isinstance(num_b, int) or isinstance(num_b, float))):
        return "Type Error: num_a and num_b must be integer or float"
    
    operator = operator.lower()
    if operator in ["add", "+"]:
        return num_a + num_b
    elif operator in ["subtract", "-"]:
        return num_a - num_b
    elif operator in ["multiply", "*"]:
        return num_a * num_b
    elif operator in ["divide", "/"]:
        if num_b == 0:
            return "Zero Division Error"
        else:
            return num_a / num_b
    else:
        return "Value Error: Operator Not Found"

# Answer:
# When num_a is not an integer or float, returns "Type Error"
# When num_b is not an integer or float, returns "Type Error"
# Successful addition when operator is "add"
# Successful addition when operator is "ADD"
# Successful addition when operator is "+"
# Successful subtraction when operator is "subtract"
# Successful subtraction when operator is "SUBTRACT"
# Successful subtraction when operator is "-"
# Successful multiplication when operator is "multiply"
# Successful multiplication when operator is "MULTIPLY"
# Successful multiplication when operator is "*"
# Successful division when operator is "divide"
# Successful division when operator is "DIVIDE"
# Successful division when operator is "/"
# When num_b is 0 and operator is division, returns "Zero Division Error"
# When operator is an invalid value, such as "elephant" or True, returns "Value Error: Operator Not Found"

# Intro to Pytest - id: 0liBZs
# Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.

# Answer:
# def test_calculate_multiplies_two_numbers():
#   assert calculate(2, 3, "*") == 6

# Intro to Pytest - id: Mv0v31
# Rearrange these lines of code so they become a valid unit test. Assume that each line would be indented correctly.

# Answer:
# def test_calculate_invalid_operator_returns_error_msg():
#   invalid_operator = "elephant"
#   error_msg = calculate(1, 1, invalid_operator)
#   assert error_msg == "Value Error: Operator Not Found"

# Intro to Pytest - id: 1R9ue5
# Read through this test report. What is the cause of the test failure?

# Answer: In the test, it calls mystery_function() with two arguments, but mystery_function() has zero parameters

# Intro to Pytest - id: fm5YB9
# In this test report, what line of what file caused the error?

# Answer: main.py, line 31

# Intro to Pytest - id: YsUv5U
# Read through this test report. What is the cause of the test failure?

# Answer: The test expects mystery_function("apples", "oranges") to return False, but it returns True

# Intro to Pytest - id: WlYb0i
# Read through this test report. What is the cause of the test failure?

# Answer: The test expects is_passenger to be True, but it's False

# Intro to Pytest - id: WzVyBp
# Read through this test report. What is the cause of the test failure?

# Answer: In mystery_function, it calls a.append(). a is the integer 100, so it doesn't have the method append

# Intro to Pytest - id: VarpJ0
# Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

# def test_returns_true():
#     result = func_that_always_returns_true()
#     assert result

# Answer:
def func_that_always_returns_true():
  return True

# Intro to Pytest - id: 621ce40e-a848-4429-a100-76e6001f77c3
# Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body, trying to write as minimal an implementation as possible, even if it's not the most robust implementation.

def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result

# Answer:
def is_odd(number):
  if number % 2 == 1:
    return True

# Intro to Pytest - id: 71615b90-7562-480f-b868-50e23812a0f3
# Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result


def test_returns_false_if_even():
    number = 6
    result = is_odd(number)
    assert not result

# Answer:
def is_odd(number):
  if number % 2 == 1:
    return True
  return False

# Intro to Pytest - id:  386b0492-77de-4132-a81c-8746090296c2
# Write a function to make the test pass. Use the information from the test to help determine what needs to be in the function body.

def test_returns_true_if_odd():
    number = 5
    result = is_odd(number)
    assert result


def test_returns_false_if_even():
    number = 6
    result = is_odd(number)
    assert not result


def test_returns_none_if_negative():
    number = -1000
    result = is_odd(number)
    assert result is None

# Answer:
def is_odd(number):
  if number < 0:
    return None
  elif number % 2 == 1:
    return True
  else:
    return False