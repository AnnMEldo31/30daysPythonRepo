import operator

# 1) Use map to call the strip method on each string in the following list:

humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]
# Print the lines of the nursery rhyme on different lines in the console.

# Remember that you can use the operator module and the methodcaller function instead of a lambda expression if you want to.

humpty_dumpty = map(operator.methodcaller("strip"), humpty_dumpty)
#or
humpty_dumpty = map(lambda strng: strng.strip(), humpty_dumpty)
#or
def line_stripper(line) :
  return line.strip()
humpty_dumpty = map(line_stripper, humpty_dumpty)

print(*humpty_dumpty, sep='\n')

print()

# 2) Below you'll find a tuple containing several names:

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
# Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list. Make sure that every name in the new list is in title case.

names = [name.title() for name in names if len(name) < 8]
print(names, sep=', ')

print()

# 3) Use filter to remove all negative numbers from the following range: range(-5, 11). Print the remaining numbers to the console.

pos_nums = filter(lambda n: n >= 0, range(-5, 11))
print(*pos_nums, sep=', ')