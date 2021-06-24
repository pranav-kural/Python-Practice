"""
The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

psuedo-code

# ask user for number
# make a guess
# ask user for input again regarding the guess
# based on user input, make another guess or exit
"""

secret_num = int(input("Please think of a number between 0 and 100!"))
low = 0
high = 100
guess = (low+high)//2

while True:

  guess_accuracy = input("Is your secret number " + str(guess) + "?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

  if guess_accuracy == 'c':
    break
  elif guess_accuracy == 'h':
    high = guess
    if low == high:
      low = 0
    guess = (low+high)//2
  elif guess_accuracy == 'l':
    low = guess
    if high == low:
      high = 0
    guess = (low+high)//2
  else:
    print("Sorry, I did not understand your input.")


print("Game over. Your secret number was:", guess)
