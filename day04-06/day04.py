# a movie title, the director’s name, the release year of the movie, and the movie’s budget
movies = [("Parasite", "Bong Joon Ho", 2019, 11_400_000)]
print(movies)

new_movie_title = input("Enter new movie's title: ")
new_movie_director = input("Name of director: ")
new_movie_release_year = int(input("Year of release: "))
new_movie_budget = int(input("Movie's budget: "))

new_movie_tuple = (new_movie_title, new_movie_director, new_movie_release_year, new_movie_budget)

# print the movie name and release year
print(f"{new_movie_tuple[0]} ({new_movie_tuple[2]})")

movies.append(new_movie_tuple)

print(movies[0])
print(movies[1])

del movies[0]
print(movies)