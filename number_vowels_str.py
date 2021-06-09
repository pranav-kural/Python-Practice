"""
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'

Program plan:
1. string "s"
2. loop through characters of string string
3. check for each character is vowel
4. if vowel, increment vowel count
5. after loop done, display vowel count

"""

# example string
s = "azcbobobegghakl"

# vowels
vowels = 'bob'

# vowel counter
numOfVowels = 0

# loop through string s
for char in s:
  if char in vowels:
    numOfVowels += 1
  
# print number of vowels
print("Number of vowels:", str(numOfVowels))