import fractions
from math import fsum
import random as r

# 1) Import the fractions module and create a Fraction from the float 2.25. 

print(fractions.Fraction(2.25))

print()

# 2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:

numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]

print(fsum(numbers))

print()

# 3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function. 

print(r.randint(1, 100))

print()

# 4) Use the randint function from the exercise above to create a new version of the guessing game we made in day 8. This time the program should generate a random number, and you should tell the user whether their guess was too high, or too low, until they get the right number.

rand_num = r.randint(1,100)

while (True) :
  guess = int(input("enter your guess (1-100): "))

  if (guess < 1 or guess > 100) :
    print("Your guess is out of range  >:(")
  elif (guess < rand_num) :
    print("Your guess is too low")
  elif (guess > rand_num) :
    print("Your guess is too high")
  else :
    print("Correct guess!")
    break