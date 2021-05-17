# Main
# exercise: Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect

# 1 - ask user to input integer
# 2 - define root and pwr
# 3 - exhaustive enumeration - for all possibilites of 0 < pwr < 6; and incrementing root by 1


user_input = int(input("Enter an integer: "))
pwr_to_start_with = int(input("Enter power to start with (range: 0 < power < 6): "))

user_input_abs = abs(user_input)

root = 0
pwr = pwr_to_start_with

while root ** pwr < user_input_abs:
  if (root + 1) ** pwr > user_input_abs:
    if pwr < 5:
      pwr += 1
      root = 0
    else:
      root += 1
  else:
    root += 1


if root ** pwr != user_input_abs:
  print("Couldn't find a perfect root for number " + str(user_input) + ", for root power " + str(pwr_to_start_with))
else:
  if user_input < 0:
    root = root * -1
  print("Result: " + str(root) + " ** " + str(pwr) + " = " + str(user_input))