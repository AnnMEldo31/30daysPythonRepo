import random


#______________________________________________________________#
# q1
def prime(l, u) :
  for num in range(l + 1, u) :
    div = 2

    while num >= div**2 :
      if num % div == 0 :
        break
      else :
        div += 1
    else :
      yield num


x = int(input("Enter lower bound: "))
y = int(input("Enter upper bound: "))

if x > y :
  temp = x
  x = y
  y = temp

print(*(prime(x, y)), sep="\n")

print()


#______________________________________________________________#
# q2
names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
  
  # names = map(lambda name: name.strip().title(), names)
print(*(name.strip().title() for name in names), sep=', ')

print()


#______________________________________________________________#
# q3
def shuffle_deck(cards) :
  deck = list(cards)
  random.shuffle(deck)
  return iter(deck)


def get_players() :
  while True:  
    no_of_players_input = input("How many players are there? ")

    try:
      no_of_players = int(no_of_players_input)
    except ValueError: 
      print("You must enter an integer value from 2 to 10")
    else:
      if no_of_players < 2:
        print("You must have minimum 2 players")
      elif no_of_players > 10:
        print("You can have maximum of 10 players")
      else:
        return no_of_players


def deal_cards(no_of_players, cards):
  deck = shuffle_deck(cards)
  
  deal_to_players(no_of_players, deck)
  deal_to_table(deck)


def deal_to_players(no_of_players, deck):
  first_cards = [next(deck) for _ in range(no_of_players)]
  second_cards = [next(deck) for _ in range(no_of_players)]

  hands = zip(first_cards, second_cards)
  
  print()

  for i, (first_card, second_card) in enumerate(hands, start=1):
    print(f"Player {i}'s hand: {first_card}, {second_card}")
  
  print()


def deal_to_table(deck):
  next(deck) # burn
  flop = ','.join(str(next(deck)) for _ in range(3))
  print(f"Flop: {flop}")

  next(deck) # burn
  print(f"Turn: {next(deck)}")

  next(deck) # burn
  print(f"River: {next(deck)}")

  print()


ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

cards = [(rank, suit) for suit in suits for rank in ranks]
# or 
# import itertools
# cards = (itertools.product(ranks, suits))

deck = shuffle_deck(cards)
no_of_players = get_players()

deal_cards(no_of_players, deck)

#______________________________________________________________#