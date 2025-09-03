#   CREATING LIST
# print("CREATING LIST\n")
# my_list = [1, 5, 10, 15, 20]
# print(my_list)

# print([True, False, False, "1"])

# my_list = list(["Lists", "are", "useful!"])
# print(my_list)

# my_list = [num for num in range (1,6)]
# print(my_list)

# ACCESSING LIST

# my_list = [num for num in range (1,6)]
# print(my_list)

# element = my_list[2]
# print(element)

# my_list = [num for num in range (1,6)]

# last_element = my_list[-1]
# print(last_element)



#  ADDIND LIST
# print("ADDING LIST\n")
# my_list = [12, 19, 26, 23]
# my_list.append(30)
# print(my_list)

# python_datatypes = ["lists"]
# python_datatypes.extend(["tuples", "sets"])
# print(python_datatypes)



# MODIFING LIST
# print("MODIFING LIST\n")
# blue_shades = ['navy', 'sky blue', 'saphire', 'powder blue', 'teal', 'turquoise']
# blue_shades[2] = 'sapphire'

# print(blue_shades)

# blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
# blue_shades[0:2] = ['denim', 'aqua']
# print(blue_shades)

# blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
# blue_shades[0:1] = ['denim', 'aqua']
# print(blue_shades)

# blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']
# blue_shades[0:4] = ['denim', 'aqua']
# print(blue_shades)

# blue_shades = ['navy', 'sky blue', 'sapphire', 'powder blue', 'teal', 'turquoise']

# blue_shades = ['cobalt', 'azure', 'ice blue']
# print(blue_shades)


# DELETING LIST
# print("DELETING LIST\n")
# space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
# print(space_movies)

# del space_movies[2]
# print(space_movies)

# space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

# del space_movies[1:3]
# print(space_movies)

# space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
# print(space_movies)

# space_movies.remove('Gravity')
# print(space_movies)

# space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']
# space_movies.clear()
# print(space_movies)

# space_movies = ['Interstellar', 'Gravity', 'The Martian', 'Apollo 13', 'Star Wars']

# removed_movie = space_movies.pop(2)
# print("The removed movie is = " + removed_movie)
# print(space_movies)



# LIST SLICING
# print("LIST SLICING\n")
# my_list = [1, 5, 10, 15, 20, 25, 30]
# print(my_list[0:2])

# my_list = [1, 5, 10, 15, 20, 25, 30]
# my_list[0:2] = 50, 55
# print(my_list)

# my_list = [1, 5, 10, 15, 20, 25, 30]
# print(my_list[1:5:2])

# my_list = [1, 5, 10, 15, 20, 25, 30]
# slice_list_from_start = my_list[:4]
# print(slice_list_from_start)

# my_list = [1, 5, 10, 15, 20, 25, 30]
# slice_list_till_end = my_list[4:]
# print(slice_list_till_end)

# my_list = [1, 5, 10, 15, 20, 25, 30]
# last_three_elements = my_list[-3:]
# print("Last three elements:", last_three_elements)

# my_list = [1, 5, 10, 15, 20, 25, 30]
# skip_every_second_from_end = my_list[-1:-6:-2]
# print(skip_every_second_from_end)

# my_list = [1, 5, 10, 15, 20, 25, 30]
# reversed_list = my_list[::-1]
# print(reversed_list)


# LIST COMPREHENSION
# print("LIST COMPREHENSION\n")
# numbers = [1, 2, 3, 4, 5]
# squares = [num ** 2 for num in numbers]

# print(squares)

# numbers = [1, 2, 3, 4, 5]
# odd_numbers = [num for num in numbers if num % 2 != 0]

# print(odd_numbers)

# words = ["hoodie", "rivers", "cat", "monitor", "bag", "cup"]
# short_words = [word for word in words if len(word) <= 5]

# print(short_words)

# numbers = [1, 2, 3, 4, 5]
# pairs = [(num, num * 2) for num in numbers]

# print(pairs)

# songs = ['Neon Lights', 'Pieces', 'Everything']
# uppercase_songs = [song.upper() for song in songs]

# print(uppercase_songs)

# my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpose = [[row[i] for row in my_matrix] for i in range(len(my_matrix[0]))]

# print(transpose)

# LIST METHOD
# print("LIST METHODS")
# python_versions = ["Python 2", "Python 3"]
# python_versions.append("Python 3.11")

# print(python_versions)

# python_modules = ["NumPy", "Pandas"]

# additional_modules = ["Matplotlib", "scikit-learn"]
# python_modules.extend(additional_modules)

# print(python_modules)

# programming_languages = ["C", "Java", "Python", "Ruby"]
# programming_languages.insert(1, "C++")

# print(programming_languages)

# frameworks = ["Django", "Flask", "Pyramid", "Flask"]
# frameworks.remove("Flask")
# print(frameworks)

# web_frameworks = ["Django", "Flask", "Pyramid", "FastAPI"]
# removed_framework = web_frameworks.pop(2)

# print(web_frameworks)

