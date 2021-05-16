x,y,z = 2,3,22

if x%3 == 0 and x > y and x > z:
  print(x)
elif y%3 == 0 and y > z:
  print(y)
elif z%3 == 0:
  print(z)
else:
  print("None of the numbers are odd")