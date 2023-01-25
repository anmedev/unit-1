# Lists Problem Statement Exercise
def dna_differences():
  dna_1 = ["G", "A", "G", "C", "C", "T", "A", "C", "T", "A", "A", "C", "G", "G", "G", "A", "T"]
  dna_2 = ["C", "A", "T", "C", "G", "T", "A", "A", "T", "G", "A", "C", "G", "G", "C", "C", "T"]
  final_dna = []

  for i in range(len(dna_1)):
    if dna_1[i] != dna_2[i]:
      final_dna.append(dna_1[i])
      final_dna.append(dna_2[i])
  print(final_dna)
dna_differences() # ["G", "C", "G", "T", "C", "G", "C", "A", "A", "G", "G", "C", "A", "C"]

# Dictionaries Exercise
time_and_colors = {"08:00": ["red", "orange", "green"], "09:00": ["red", "orange"], "10:00": ["blue"], "11:00": ["blue", "green"], "12:00": ["blue", "gray"], "13:00": ["red", "blue"], "14:00": ["white"], "15:00": ["green", "white"], "16:00": ["white", "black"], "17:00": ["yellow", "black"], "18:00": ["white", "green", "gray", "red", "blue"]}
color_frequency = {"red": 4, "blue": 5, "yellow": 1, "green": 4, "orange": 2, "gray": 2, "black": 2, "white": 4}