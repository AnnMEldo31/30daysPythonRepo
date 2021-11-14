# 1) It should be able to accept a card number from the user. For this project, you can assume that the number will be entered as a single string of characters (i.e. there won't be any spaces between the numbers). However, you should be able to accept a card number with spaces at the start or end of the string.

# If you want to challenge yourself, you should try to be more versatile with regards to the format that you accept card numbers in.

# You may want to turn the user's input into a list of numbers, as that will make it easier to work with.

credit_card = list(input("Enter credit card number: ").strip())

# 2) The program should validate that card number using the Luhn algorithm described above. You should implement this algorithm yourself.

# 1. Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
# 2. Reverse the order of the remaining digits.
# 3. For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9, subtract 9 from those numbers.
# 4. Add together all of the results and add the checking digit.
# 5. If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

last_digit = int(credit_card.pop())
credit_card.reverse()

processed = []

for order, digit in enumerate(credit_card) :
  if order % 2 == 0 :
    processed.append((int(digit) * 2) % 9)
  else :
    processed.append(int(digit))

sum = sum(processed) + last_digit

if (sum % 10 == 0) :
  print("Valid")
else :
  print("Invalid")