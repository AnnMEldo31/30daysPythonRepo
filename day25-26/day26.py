from collections import namedtuple, defaultdict
from operator import mul
from functools import partial

'''
1) Define a Movie tuple using namedtuple that accepts a title, a director, a release year, and a budget. Prompt the user to provide information for each of these fields and create an instance of the Movie tuple you defined.

2) Use a defaultdict to store a count for each character that appears in a given string. Print the most common character in this dictionary.

3) Use the mul function in the operator module to create a partial called double that always provides 2 as the first argument.

4) Create a read function using a partial that opens a file in read ("r") mode.
'''
#______________________________________________________________________#
# q1

Movie = namedtuple("Movie", ["title", "director", "release_year", "budget"])

title = input("Enter title: ").strip().title()
director = input("Enter director's name: ").strip().title()
try:
  year = int(input("Enter release year: "))
except ValueError:
  year = 2022
try:
  budget = int(input("Enter budget: "))
except ValueError:
  budget = 1000000

newMovie = Movie(title, director, year, budget)
print(f"{newMovie.title} ({newMovie.release_year}) by {newMovie.director} with budget of ${newMovie.budget}")

print()

#______________________________________________________________________#
# q2

str = 'liiiiiiiiiiiiiiiiiiittle         ssssst'

characterCount = defaultdict(int)

for ch in str:
  characterCount[ch] += 1

print(max(characterCount, key=lambda ch: characterCount[ch]))

print()

#______________________________________________________________________#
# q3

double = partial(mul, 2)
print(double(4))

print()

#______________________________________________________________________#
# q4

read = partial(open, mode="r")
with read("klog.txt") as f:
  print(f.readlines())