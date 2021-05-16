# 1 - define variables
# 2 - start the loop
# 3 - ask user for input
# 4 - if user enters "end" - end the program; if not proceed
# 4 - check for each input, if user entered "end"
# 5 - if not "end" - convert input and store the number
# 6 - check if number entered is odd number, and if it is larger than previous input
# 7 - if both conditions met, save the number
# 8 - if not, continue asking again for input


largest_odd = 0
user_input = ""

while (user_input != "end"):
  if user_input != "":
    user_input = input("Enter the next number: ")
  else:
    print("Welcome! This program will take integers as input and give the largest odd number in the end, if there is any. Once you're done entering integers, type 'end' to run the program and see the result. Have fun!")
    user_input = input("Enter the first integer to start: ")
    
  if (user_input != "end"):
    current_num = int(user_input)
  
    if current_num % 3 == 0 and current_num > largest_odd:
      largest_odd = current_num

if largest_odd != 0:
  print("Largest odd among the numbers you provided is:", str(largest_odd))
else:
  print("Oops! No odd number among the numbers you provided!")