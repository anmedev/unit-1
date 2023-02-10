# Expressions and Statements - id: e255bf2d-f703-4a22-ba13-f142584bba93
# There is an expression on line 2. Identify the expression on line 2.
test_num = 5
if test_num > 10:
  print("Bigger than ten!")

# test num > 10

# Literals - id: f07c693b-b2f2-4e16-a114-74cf6fcfe43a
# Using the code snippet below, identify at least 1 literal:
test_num = 5
if test_num > 10:
  print("Bigger than ten!")

# "Bigger than ten!", other literals include 5 and 10

# Fundamentals Vocabulary - id: 82df3237-9f64-4ddc-b5a2-843f53430b15
# What is a statement?
# a unit of code that performs an action

# Fundamentals Vocabulary - id: FsVllh
# What is the value of the expression int("100")?
int("100") # 100

# Fundamentals Vocabulary - id: PLQcV3
# What is the value of the expression int("-99")?
int("-99") # -99

# Fundamentals Vocabulary - id: unzxTM
# What is the value of the expression int(True)?
int(True) # 1

# Fundamentals Vocabulary - id: JT1AQl
# What is the value of the expression int(False)?
int(False) # 0

# Fundamentals Vocabulary - id: v5J2Qt
# What is the value of the expression int("Hello, casting!")?
# int("Hello, casting!") # ValueError: invalid literal for int() with base 10: 'Hello, casting!'

# Fundamentals Vocabulary - id: fsmTXv
# What is the value of the expression float("100")?
float("100") # 100.0

# Fundamentals Vocabulary - id: 3uz8do
# What is the value of the expression float(10/2)?
float(10/2) # 5.0

# Fundamentals Vocabulary - id: Sb9SHJ
# What is the value of the expression float(True)?
float(True) # 1.0

# Fundamentals Vocabulary - id: LcXazs
# What is the value of the expression float("Hello, casting!")?
# float("Hello, casting!") # ValueError: could not convert string to float: 'Hello, casting!'

# Fundamentals Vocabulary - id: GfI4jM
# What is the value of the expression str(100)?
str(100) # "100"

# Fundamentals Vocabulary - id: yzgREY
# What is the value of the expression str(True)?
str(True) # "True"

# Fundamentals Vocabulary - id: pw72Cy
# What is the value of the expression str([True, 0, 55.55])?
str([True, 0, 55.55]) # "[True, 0, 55.55]"

# Fundamentals Vocabulary - id: qgPojl
# What is the value of the expression bool(100)?
bool(100) # True

# Fundamentals Vocabulary - id: TnVLkK
# What is the value of the expression bool(-99)?
bool(-99) # True

# Fundamentals Vocabulary - id: gmV017
# What is the value of the expression bool("Hello, string!")?
bool("Hello, string!") # True

# Fundamentals Vocabulary - id: uMYUNK
# What is the value of the expression bool([])?
bool([]) # False

# Fundamentals Vocabulary - id: 50Wo1z
# What is the value of the expression bool(None)?
bool(None) # False

# Fundamentals Vocabulary - id: b2c12540-3562-4fe1-aedc-54332282b9aa
# Which of the following options is a dictionary literal?
{
    "apple": "gala apple",
    "orange": "sumo orange",
    "pear": "anjou pear",
}
{"apple": "gala apple"}

# Fundamentals Vocabulary - id: A1c1Qx
# Which of the following are literals?
"Welcome! Make yourselves comfortable!"
["magenta", "purple", "blue"]
None

# Fundamentals Vocabulary - id: 5uhdzz
# Which of the following are literals?
87
"87"
True
[]

# Fundamentals Vocabulary - id: S9Y41l
# Which of the following are expressions, and not statements? Assume that all variables are properly defined.
# sum > total
# 5 - 10
# is_eligible and not is_expired
# False or (is_eligible and not is_expired)

# Fundamentals Vocabulary - id: 7kQfOC
# What does this line of code print to the console?
print(type("I'm programming!")) # <class 'str'>

# Fundamentals Vocabulary - id: LyP1Nn
# What does this line of code print to the console?
age = 99
print(f"Tomorrow, I will be {age + 1} years old!") # Tomorrow, I will be 100 years old!

# Fundamentals Vocabulary - id: LyP1Nn
# What does this line of code print to the console?
age = 99
print("Tomorrow, I will be {age + 1} years old!") # Tomorrow, I will be {age + 1} years old!

# Fundamentals Vocabulary - id: SBSiYv
# What does this line of code print to the console?
age = 99
print("Tomorrow, I will be", age + 1, "years old!") # Tomorrow, I will be 100 years old!

# Fundamentals Vocabulary - id: VNJdEq
# What does this line of code print to the console?
age = 99
print("The current value of age is: ", age) # The current value of age is: 99

# Fundamentals Vocabulary - id: 4jUlbM
# What is the command line command to open the Python 3 interpreter?
# python3

# Fundamentals Vocabulary - id: NU7rOw
# Imagine that we are running the Python 3 interpreter in a Terminal. What are all of the valid commands or key combinations to exit the interpreter, and return to the command line?

# exit()
# quit()
# ctrl D

# Fundamentals Vocabulary - id: NU7rOw
# Consider this code. Running this code produces the error TypeError: can't multiply sequence by non-int of type 'str'. Which of these options most accurately describes the cause of this error?
# n1 = input("enter a number: ")
# n2 = input("enter another number: ")
# def multiply(n1, n2):
#  	return n1*n2
# multiply(n1,n2)

# The function input() always gives back a string. The values of n1 and n2 are strings. Multiplication in the line n1*n2 gives an error, because mulitplying strings isn't possible.

