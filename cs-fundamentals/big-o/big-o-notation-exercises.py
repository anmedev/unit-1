# Time/Space Complexities Worst-to-best- id: d2d156f6-aaab-4aba-9cf7-b9cdaceed013
# Arrange the following complexities from worst to best.

# Answer:
# O(2n) - exponential
# O(n2) - quadratic
# O(n log n) - log linear
# O(n) - linear
# O(log n) - logarithmic
# O(1) - constant

# Purpose of Big-O Notation - id: db5bbef4-04da-4474-8aa1-5a86e7047e6a
# Big O notation serves to:
# Calculate the exact run time or space usage of a given algorithm
# Describe how the algorithm performs in terms of both space and time as the input size increases
# Describe only how well an algorithm will perform in terms of speed as the input size increases
# Describe only how well an algorithm will perform in terms of memory usage as the input size increases

# Answer: Describe how the algorithm performs in terms of both space and time as the input size increases

# Pick the best performing algorithm - id: 6b2620b0-f164-4722-8a55-a000a6b3690a
# Imagine creating an app that allows a user to store all of their contacts and contact information. There is a feature that allows users to search for a specific contact. Given the following algorithms for this search feature, which is the best choice in terms of time and space complexity?

# Store all contacts in a list and seach for each contact, iterating from beginning until end until the contact is found or the list is completely searched. O(n)
# Store all contacts in a dictionary with the contact name as a key and retrieve contacts using the name. O(1)
# Store all contacts in a list sorted by names and search for a contact by looking at the middle contact. If that is the desired contact return them. If the desired contact comes later repeat the search in the 2nd half of the list, otherwise repeat the search in the 1st half of the remaining contacts. Repeat until the contact is found or there are no more contacts left to search. O(log n).

# Answer: Store all contacts in a dictionary with the contact name as a key and retrieve contacts using the name. O(1)