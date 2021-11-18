# 1) Create an empty set and assign it to a variable.

new_set = set()
print(new_set)

print()

# 2) Add three items to your empty set using either several add calls, or a single call to update.

new_set.add("1st")
new_set.update(["2nd", "3rd"])

print(new_set)

print()

# 3) Create a second set which includes at least one common element with the first set.

second_set = {"1st", "object", "kale"}
print(second_set)

print()

# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.

print(new_set.union(second_set))
print(new_set.symmetric_difference(second_set))
print(new_set.intersection(second_set))

print()

# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.

number_sequence = set(range(11, 20))
number = int(input("Enter a number: "))
if number in number_sequence :
  print("Number in range")
else :
  print("Number not in range")

# If you want an extra challenge, also tell the user if their number was too high or too low.

  if number < 11 :
    print("Too low number")
  else :
    print("Too high number")

print()