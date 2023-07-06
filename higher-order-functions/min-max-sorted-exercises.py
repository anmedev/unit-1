# Passing Functions As Parameters: Max, Min, and Sort - id: a1681db0-2b2d-48cb-bdf5-2f434cc04676
INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0,
    "release_year": 1999
}
INTRIGUE_2 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0,
    "release_year": 2022
}
ACTION_1 = {
    "title": "2 JavaScript 2 React",
    "genre": "Action",
    "rating": 4.2,
    "release_year": 2015
}
ACTION_2 = {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5,
    "release_year": 2013
}

movies = [INTRIGUE_1, INTRIGUE_2, ACTION_1, ACTION_2]

# Which of the following will return the list of movies sorted by their "rating".
# Answer: sorted(movies, key=get_rating)