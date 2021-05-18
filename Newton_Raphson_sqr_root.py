

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0

# theorem that implies that if a value, call it guess, is an
# approximation to a root of a polynomial (p), then guess – p(guess)/p’(guess), where p’ is
# the first derivative of p, is a better approximation

epsilon = 0.01
k = 24.0
guess = k/2.0
NumGuesses = 0

while abs(guess*guess - k) >= epsilon:
  guess = guess - (((guess**2) - k)/(2*guess))
  NumGuesses += 1

print('Square root of', k, 'is about', guess)
print('Number of guesses: ', NumGuesses)