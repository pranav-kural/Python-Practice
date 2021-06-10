"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Algorithm:
1 - s is lower case string
2 - check characters in sets of 3, starting from beginning of string s, and compare against 'bob'
3 - if this subset of string equal to 'bob', increment bob counter
4 - return bob counter 

"""

s = 'obnbobobobobbobobboboboboboboboboboooboo'

# bob counter
bobCounter = 0

# start and end indexes to get subset of string
# intial value 0, 3 - first three characters from s
startIndex, endIndex = 0, 3

# check for each subset of 3 characters from string s
"""
while endIndex <= len(s):
  if s[startIndex:endIndex] == "bob":
    bobCounter += 1
  startIndex += 1
  endIndex += 1
"""
print(len(s))

for i in range(len(s)):
  if s[i:i+3] == "bob":
    bobCounter += 1

# print result
print("Number of times bob occurs is:", str(bobCounter))
