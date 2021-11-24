# 1) Create a short program that prompts the user for a list of grades separated by commas. Split the string into individual grades and use a list comprehension to convert each string to an integer. You should use a try statement to inform the user when the values they entered cannot be converted.

grade_list = input("Enter comma-separated list of grades: ").strip().split(',')
try :
  grade_list = [int(grade.strip()) for grade in grade_list]
  print(grade_list)
except ValueError :
  print("Your entered values could not be converted")

print()

# 2) Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.

def first_grade(grading_list) :
  try :
    return grading_list[0]
  except TypeError:
    print("Not a list")
    return 0
  finally :
    return 8

print(first_grade(grade_list))
print(first_grade(77))
# in both cases, finally return statement is executed

# 3) Imagine you have a file named data.txt with this content:

# There is some data here!

# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't exist. Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.

# When files don't exist when you try to open them, the exception raised is FileNotFoundError.

try :
  with open("data.txt", "r") as f :
    data = f.readlines()
  print(data)
except FileNotFoundError :
  print("File not found")