from random import sample

'''
1) Write a function that prompts the user for their name and then greets them. You should process the string by removing any whitespace and converting the string to title case.

If after processing the string you're left with an empty string, the function should replace the empty string with "World" in the output.

2) Write a function to determine whether or not a string contains exclusively ASCII letters (a to z in either upper or lowercase).

Hint: You should look at the constants in the string module. 

3) Use the sample function in the random module to create three lists, each containing fifteen numbers from 1 to 100 (inclusive). Sort each of these lists into descending order (largest first), and then truncate each list so that only 5 items remain in each.
'''
#________________________________________________________________#
# q1

def greet() :
  name = input("Please enter your name: ").strip().title() or "World"
  print("Hello " + name)

# greet()

print()

#________________________________________________________________#
# q2

# my previous solution
'''def is_ASCII(str) :
  for ch in str:
    if ch not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
      print("Not only ASCII letters")
      break
  else:
    print("Only ASCII letters")'''

# i stand bettered
def is_ASCII_letters(str) :
  return all(ch in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for ch in str)

def is_ASCII(str) :
  if is_ASCII_letters(str):
    print(f"{str}: ascii letters only")
  else :
    print(f"{str}: not only ascii letters")

is_ASCII("hello world")
is_ASCII("Sally")
is_ASCII("1hdiie")
is_ASCII("hfiw(jflwi")

print()

#________________________________________________________________#
# q3

li = [sample(range(1, 101), 15) for _ in range(3)]

for numset in li:
  numset.sort(reverse=True)
  del numset[5:]

print(li)