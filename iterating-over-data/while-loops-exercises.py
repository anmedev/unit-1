# While Loops - id: AJC4nw
# Fix this loop so it loops while i is less than 5 .
# def loop_until_five():
#     i = 0
#     while False:
#         i += 1
#     return i
# result = loop_until_five()

# Answer:
def loop_until_five():
    i = 0
    while i < 5:
        i += 1
    return i
result = loop_until_five()
print(result)

# While Loops - id: jMroBQ
# Think about the function named loop_until_five() from the previous question. What value does loop_until_five() return?

# Answer: 5

# While Loops - id: UZgKoW
# Which of these loop table options most accurately describes this loop?
i = 0
result = None

while i < 5:
    if (i % 2) == 0:
        result = True
    else:
        result = False
    i += 1

# Answer: Loop Table Durian -- see exercise for loop table option