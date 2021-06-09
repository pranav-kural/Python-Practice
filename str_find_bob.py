"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Algorithm:
1 - s is lower case string
2 - check characters in sets of 3, starting from beginning of string s, and compare against 'bob'
3 - if this subset of string equal to 'bob', increment bob counter
4 - return bob counter 

"""

s = 'azcbobobegghakl'

# bob counter
bobCounter = 0


# print result
print("Number of times bob occurs is:", str(bobCounter))
