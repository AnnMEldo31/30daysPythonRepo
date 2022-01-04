#______________________________________________________________#
# q1
# Ask the user for an integer between 1 and 10 (inclusive). If the number they give is outside of the specified range, raise a ValueError and inform them that their choice was invalid.

num = int(input("Enter an integer between 1 to 10 (inclusive): "))
if num < 1 or num > 10:
  raise ValueError("Invalid choice")

print()

#______________________________________________________________#
# q2
# Below you'll find a divide function. Write exception handling so that we catch ZeroDivisionError exceptions, TypeError exceptions, and other kinds of ArithmeticError.

# divide(a, b)
# 	print(a / b)

# Types of errors
# +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError

def divide(a, b):
  try:
    print(a / b)
  # except ZeroDivisionError as zerError:
  #   print(f"Zero Error: {zerError}")
  except TypeError as typeError:
    print(f"Type Error: {typeError}")
  except ArithmeticError as arthError:
    print(f"Arithmetic Error: {arthError}")


divide(10, 2)
divide(10, 0) # zerError
divide('a','b') # typeError

print()

#______________________________________________________________#
# q3
# Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances of KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused this issue. Once you have written to the log file, reraise the original exception.

# def itemgetter(collection, identifier):
# 	return collection[identifier]

def exceptionLogger(ex, fn, **kwargs):
  values = ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
  
  with open("day22-24/day24/log.txt","a") as log_file:
    log_file.write(f"Exception: {ex}\n\tFunction: {fn}\n\tArguments: {values}\n")
    log_file.close()


def itemgetter(collection, identifier):
  try:
    return collection[identifier]
  except (KeyError, IndexError) as ex:
    exceptionLogger(ex, "itemgetter", collection=collection, identifier=identifier)    
    raise


array1 = [12, 14, 18, 17]
print(itemgetter(array1, 5))

array2 = {"a":1,"b":2,"c":3,"d":4}
print(itemgetter(array2, "ab"))