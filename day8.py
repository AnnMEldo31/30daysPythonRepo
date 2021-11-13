# 1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

import random
num = random.randrange(2,100)

guess = int(input("We have a number between 1 and 100. Try to guess it and enter your guess: "))

while num != guess :
  if (guess <= 1) or (guess >= 100) :
    print("Guessed number must be between 1 and 100, with and 1 and 100 not included")
  elif num < guess :
    print("Too high")
  else :
    print("Too low")
  guess = int(input("Please enter your guess again: "))
print("Correct guess!")

print()

# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.

for c in "Python" :
  if c == 'o' :
    continue
  print(c)

for c in "Python" :
  if c == 'o' :
    continue
  print(c,end='')

print()

# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.

# number between 1 and 100 (1 and 100 not included)
for num in range(2, 100) :

  # we dont care for division by 1 since all numbers are divisible by 1, so we start with 2
  div = 2

  while num >= div**2 :
    if num % div == 0 :
      break
    else :
      div += 1
  else :
    print(num)

  num += 1