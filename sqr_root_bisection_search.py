# bisection search to find sqaure root

x = 25
x_abs = abs(x)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x_abs)
ans = (high + low)/2.0

while abs(ans**2 - x_abs) >= epsilon:
  print('low =', low, 'high =', high, 'ans =', ans)
  numGuesses += 1
  if ans**2 < x_abs:
    low = ans
  else:
    high = ans
  ans = (high + low)/2.0

print('numGuesses =', numGuesses)
if x < 0:
  ans = -ans
print(ans, 'is close to square root of', x)