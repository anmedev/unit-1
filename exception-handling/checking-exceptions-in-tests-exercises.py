# Checking Exceptions in Tests - id: 8HwyKa
# What is the function call that will raise an exception?

def test_check_is_phone_num_valid():
    phone_num = 777-888-9999
    with pytest.raises(ValueError):
        is_valid = is_phone_num_valid(phone_num)

# Answer: is_phone_num_valid(phone_num)

# Checking Exceptions in Tests - id: wrXI7Z
# What is the kind of exception we're expecting?

def test_check_is_phone_num_valid():
    phone_num = 777-888-9999
    with pytest.raises(ValueError):
        is_valid = is_phone_num_valid(phone_num)

# Answer: ValueError

# Checking Exceptions in Tests - id: TmFBrt
# What is the function call that will raise an exception?

def test_add_student_to_roster():
    roster = {}
    student = "Cordelia Wang"
    with pytest.raises(AttributeError):
        add_student_to_roster(roster, student)

# Answer: add_student_to_roster(roster, student)

# Checking Exceptions in Tests - id: z4Qv6S
# What is the kind of exception we're expecting?

def test_add_student_to_roster():
    roster = {}
    student = "Cordelia Wang"
    with pytest.raises(AttributeError):
        add_student_to_roster(roster, student)

# Answer: AttributeError