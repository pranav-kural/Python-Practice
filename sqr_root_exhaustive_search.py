
x = 25
epsilon = 0.01
step = epsilon**3
numGuesses = 0
ans = 0.0

while abs(ans**2 - x) >= epsilon and ans * ans <= x:
  ans += step
  numGuesses += 1

print('numGuesses =', numGuesses)
print(ans**2 - x)

if abs(ans**2 - x) >= epsilon:
  print('Failed on square root of', x)
else:
  print(ans, 'is close to square root of', x)
