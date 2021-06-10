"""
Assume s is a string of lower case characters.

Write a program that logs the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should log

Longest substring in alphabetical order is: beggh

In the case of ties, log the first substring. For example, if s = 'abcbcd', then your program should log

Longest substring in alphabetical order is: abc
"""

"""
str_longest_substring_alphb_order.py

Given a string 's' containing all lower case characters, prints the longest substring of 's' in which the letters occur in alphabetical order

"""
# for logging to console - for testing and understanding
log = print

# pre-defined s
s = "azcbobobegghakl"

# iterate through string s each character at a time from right
currLongestSubstr = ""

for i in range(len(s)):

    # temporarily hold characters coming in alphabetic order
    charsMatched = ""

    log("*"*40)
    log("Outer loop iteration")
    log("Current char:", s[i])

    # hold the prev character for comparison later on
    prevChar = s[i]

    # iterate through substring of s starting from s[i]
    for currChar in s[i:]:
        log("-"*10)
        log("Inner loop iteration")
        log("prevChar:", prevChar, "currChar:", currChar)

        """
        compare UNICODE numbers of current character, and previous charater
        if unicode number of current character higher than previous character, 
        means it's in alphabetical order
        """
        if ord(currChar) >= ord(prevChar):
            # update charsMatched with current character
            charsMatched += currChar
            

            log("lenns", str(len(charsMatched)), str(len(s[i:])))

            """
            Below conditional to handle situations where all letters in a substring are 
            in alphabetical order. In such situation, iteration can be stopped, since it would
            be the longest alphabetical substring
            """
            if len(charsMatched) == len(s[i:]) and len(charsMatched) > len(currLongestSubstr):
                # update currLongestSubstr if current charsMatched are longer
                currLongestSubstr = charsMatched
                break
        else:
            # update currLongestSubstr if current charsMatched are longer
            if len(charsMatched) > len(currLongestSubstr):
                currLongestSubstr = charsMatched

            # reset charsMatched for next iteration
            charsMatched = ""
            log("^"*10)
            log("currLongestSubstr:", currLongestSubstr)
            break
        
        # update prevChar for next iteration
        prevChar = currChar

        log("charsMatched: ", charsMatched)
    # end of nested for loop

    # if all characters in s starting from index i are in alphabetical order, break out of loop
    if len(currLongestSubstr) == len(s[i:]):
        break
   
    log("currLongestSubstr:", currLongestSubstr)
# end of outer for loop

# print result
print("Longest substring in alphabetical order is:", currLongestSubstr)


