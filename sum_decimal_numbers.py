# Lesson 3 - For loop
#exercise: Let s be a string that contains a sequence of decimal numbers
#separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
#the sum of the numbers in s

#list_of_nums = input("Enter list of decimal numbers (separated by comma, no spaces): ")

sum_of_nums = 0
num_to_add = ""

for each_num in "1.23,2.4,3.123":
  print("each num", each_num)

  if each_num == '.'o:
    num_to_add += each_num
  elif each_num == ','


  sum_of_nums += float(each_num)

print("Sum of all provided numbers (" + list_of_nums + ") is: ", sum_of_nums)