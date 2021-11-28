#1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
greeting1 = ["Hello", "Hi"]
greeting2 = ["Hello", "Hi"]
print(greeting1)
print(greeting2)
print(f"==? {greeting1 == greeting2}")
print(f"IDs: {id(greeting1)}, {id(greeting2)}")
if id(greeting1) == id(greeting2) :
  print("is will show True")
else :
  print("is will show False")
print(f"is? {greeting1 is greeting2}")

numbers = [1, 2, 3, 4]
numbers_copy = numbers
numbers.append(5)
print(numbers)
print(numbers_copy)
print(numbers is numbers_copy)

print()

# 2) Try to use the is operator or the id function to investigate the difference between this:
#   numbers = [1, 2, 3, 4]
#   new_numbers = numbers + [5]
# And this:
#   numbers = [1, 2, 3, 4]
#   numbers.append(5)
# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(numbers is new_numbers)

numbers2 = [1, 2, 3, 4]
id1 = id(numbers2)
numbers2.append(5)
id2 = id(numbers2)
print(id1 == id2)
print()

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
num = float(input("Enter a number: "))
if num < 0 :
  print(f"{num} is negative")
elif num > 0 :
  print(f"{num} is positive")
else :
  print(f"Number is zero")
print()

# 4) Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.
hours_worked = float(input("Enter number of hours worked this week: "))
hourly_wage = float(input("Enter hourly wage: "))
if hours_worked > 40.0 :
  print("Overtime due.")
  salary_due = (40.0 * hourly_wage) + ((hours_worked - 40.0) * hourly_wage * 110 / 100)
  print(f"Total Salary = ${salary_due:.2f}")
else :
  salary_due = hours_worked * hourly_wage
  print(f"Total Salary = ${salary_due:.2f}")