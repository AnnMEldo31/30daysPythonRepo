# 1. Calculate the average budget of all movies in the data set.
# 2. Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
# 3. Print out how many movies spent more than the average you calculated.

# Extra:
# 1. Ask the user how many movies they want to add to the list.
# 2. Use range and a for loop to perform some option the specified number of times.
# 3. Ask the user for a movie name and budget during each iteration of the loop, and append a tuple to the movies list containing this information.

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

new_movie_count = int(input("Enter how many new movies you wish to add: "))

for _ in range(new_movie_count):
    name = input("Enter new movie name: ")
    budget = int(input("Enter new movie budget: "))
    new_movie = (name, budget)
    movies.append(new_movie)

total_budget = 0

for movie in movies :
  total_budget += movie[1]
average = int(total_budget / len(movies))
print(f"Average movie budget: ${average:,}")

print()

no_of_high_budget_movies = 0

print("High Budget movies: ")
for movie in movies :
  if movie[1] > average :
    print(f"{movie[0]}, higher than avg. by ${movie[1] - average:,}")
    no_of_high_budget_movies += 1

print()

print(f"Number of high budget movies = {no_of_high_budget_movies}")