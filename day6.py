# 1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

for employee in employees :
  wages_due = employee[1] * employee[2]
  print(f"{employee[0]} is owed ${wages_due:,.2f}")

print()

# 2) For the employees above, print out those who are earning an hourly wage above average.

# Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.

total_wages = 0.0
no_of_employees = 0

for employee in employees : 
  no_of_employees = no_of_employees + 1
  total_wages = total_wages + (employee[1] * employee[2])
average = total_wages / no_of_employees

print("Employees who earn above average")
for employee in employees :
  if (employee[1] * employee[2]) > average :
    print(employee[0])