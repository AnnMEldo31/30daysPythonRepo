# 1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.

def exponentiate(base, power) :
  return base ** power

print(exponentiate(2, 3))

print()

# 2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.

def process_string(strng) :
  return strng.strip().lower()

print(process_string("   Hello!!!    "))

print()

# 3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:

# ("Tom Hardy", "English", 42)  # name, nationality, age
# You can choose whatever key names you like for the dictionary.

def actor_dictnry(actor_tup) :
  name, nationality, age = actor_tup
  return {
    "name": name,
    "nationality": nationality,
    "age": age
  }

print(actor_dictnry(("Tom Hawks", "Horation", 76)))

print()

# 4) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def is_prime(num) :
  if num < 1:
    print("Positive numbers only")
    return False
  elif num == 1:
    return False
  
  divisor = 2

  while num >= divisor ** 2 :
    if num % divisor == 0 :
      return False
    divisor += 1
  return True

print(is_prime(1))
print(is_prime(2))
print(is_prime(9))
print(is_prime(0))