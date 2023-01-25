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