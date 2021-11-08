# Day 3 Project
#
# Take in employee name, hours worked and hourly wage
# Process them appropriately
# Print out string in the format below:
# "Regina George earned $800 this week."

employee_name = input("Enter your name: ").strip().title()
hours_worked = input("Enter number of hours worked this week: ")
hourly_wage = input("Enter your hourly wage: ")

# calculating earned wages
earned_wages = float(hourly_wage) * float(hours_worked)

# printing string with formatting for the wages
print(f"{employee_name} earned ${earned_wages:.,2f} this week.")
    # :.,2f   --->   gives two digits after decimal point with comma separation e.g. 1,030.50 