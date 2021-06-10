s = "azcbobobegghakl"
currLongestSubstr = ""
for i in range(len(s)):
    charsMatched, prevChar = "", s[i]
    for currChar in s[i:]:
        if ord(currChar) >= ord(prevChar):
            charsMatched += currChar            
            if len(charsMatched) == len(s[i:]) and len(charsMatched) > len(currLongestSubstr):
                currLongestSubstr = charsMatched
                break
        else:
            currLongestSubstr, charsMatched = charsMatched if len(charsMatched) > len(currLongestSubstr) else currLongestSubstr, ""
            break        
        prevChar = currChar
    if len(currLongestSubstr) == len(s[i:]):
        break
print("Longest substring in alphabetical order is:", currLongestSubstr)