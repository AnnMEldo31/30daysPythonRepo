# 1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember that we can use the sum function to add the values in an iterable.

def add_numbers(*numbers) :
  return sum(numbers)

print(add_numbers(7, 8, 23, 14))

print()

# 2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user. Your output should indicate which values were provided as positional arguments, and which were provided as keyword arguments.

def pos_and_kw_args(*args, **kwargs) :
  args = [repr(arg) for arg in args]
  print(f"Positional arguments are: {', '.join(args)}")
  print("\nKeyword Arguments are: ")
  
  kwargs = [f"{kwarg_key}={repr(kwarg_value)}" for kwarg_key, kwarg_value in kwargs.items()]
  print(', '.join(kwargs))

pos_and_kw_args(7, "ash", 'halo', 17, country='Bulgary', rollno=887, rand=lambda x: x*2)

print()

# 3) Print the following dictionary using the format method and ** unpacking.

country = {
  "name": "Germany",
  "population": "83 million",
  "capital": "Berlin",
  "currency": "Euro"
}

country_details = """{name} has a population of {population}. 
It's capital is {capital}. 
The {currency} is its national currency."""

print(country_details.format(**country))

print()

# 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas. You will have to provide an argument for print function's sep parameter for this exercise.

print(*range(1,21), sep=", ")

print()

# 5) Modify your code from exercise 4 so that each number prints on a different line. You can only use a single print call.

print(*range(1,21), sep="\n")