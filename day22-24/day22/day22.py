from itertools import cycle


# q.1&2
numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]

x = map(sum, numbers)

print(next(x))
print(next(x))

print()


# q3
emp = cycle('ABC')
day_wk = cycle(['M', 'T', 'W', 'T', 'F', 'S', 'S'])
for day_no in range(0, 31):
  print(f"{day_no}, {next(day_wk)}: {next(emp)}")