# Function Error - id: e205de80-0a88-486d-a842-30a29d5f896e
# Predict: What error we will see and why we will see it?
# sing_happy_birthday("Melinda")
# sing_happy_birthday("Kerry")

# def sing_happy_birthday(name):
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print(f"Happy birthday, dear {name}")
#     print("Happy birthday to you")

# NameError because the function is invoked before it's defined.

# Function Syntax - id: dd40bdc9-236d-444c-afb2-7cc45cdd9970
# Which of these has correct syntax in its function signature and its function body?
def convert_to_fahrenheit(deg_celsius):
    result = (deg_celsius * 1.8) + 32
    return result
print(convert_to_fahrenheit(32))