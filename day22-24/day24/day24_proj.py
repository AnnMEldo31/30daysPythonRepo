import random
import argparse

#parser config
parser = argparse.ArgumentParser(description="A program to simulate rolling dice. User is given option to specify number of dce, number of sides of a die, number of times to roll the dice and where to log results")

#parser arguments
parser.add_argument(
  "dice", 
  type=str, 
  help="Dice representation as xdy where x, y are integers representing number of dice and number of sides of a die respectively"
)

parser.add_argument(
  "-l",
  "--log",
  type=str,
  metavar="path",
  default="day22-24/day24/roll_log.txt",
  help="Specify logging file name"
)

parser.add_argument(
  "-r",
  "--repeat",
  type=int,
  default=1,
  metavar="number",
  help="Specify number of times to roll the dice"
)


# functions for dice roll
# parse dice
def diceParse(diceRep):
  try:
    quantity, sides = [int(arg) for arg in diceRep.split("d")]
  except ValueError:
    raise ValueError("Invalid dice representation. Dice representation is xdy where x, y are integers representing number of dice and number of sides of a die respectively")
  
  return quantity, sides

#roll dice
def diceRoll(quantity, sides) :
  rollResults = [random.randint(1, sides) for _ in range(quantity)]
  return rollResults


# output
# template
record = '''Rolls: {}
Total: {}
Average: {:.2f}
'''

# print to screen
def results_screen(rolls, total, avg) :
  rolls_string = ', '.join([str(roll) for roll in rolls])
  return record.format(rolls_string, total, avg)


# logging
def results_log(rolls, total, avg, log_file) :
  with open(args.log, "a") as log_file:
    log_file.write(results_screen(rolls, total, avg))
    log_file.write('-' * 30 + '\n')


#____________________________________________________________________________#
args = parser.parse_args()

quantity, sides = diceParse(args.dice)

for _ in range(args.repeat):
  rolls = diceRoll(quantity, sides)
  total = sum(rolls)
  avg = float(total) / len(rolls)

  # print to screen
  print(results_screen(rolls, total, avg))

  # logging
  results_log(rolls, total, avg, args.log)