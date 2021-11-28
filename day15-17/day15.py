# 1) Convert the following for loop into a comprehension:

# numbers = [1, 2, 3, 4, 5]
# squares = []

# for number in numbers:
# 	squares.append(number ** 2)

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print(squares)

# 2) Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.

# movie = {
# 	"title": "thor: ragnarok",
# 	"director": "taika waititi",
# 	"producer": "kevin feige",
# 	"production_company": "marvel studios"
# }
# Remember that iterating over a dictionary only gives us the keys by default. You can use the items method to get the keys and the values.

movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

movie = {
  m_key : m_val.title()
  for m_key, m_val in movie.items()
}

print(movie)