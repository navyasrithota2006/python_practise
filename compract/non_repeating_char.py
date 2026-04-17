'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
'''
from collections import Counter

 # counter always results in dict like objects where it has few other features most_common() ,elements() etc 
def firstuniquechar(s):
    count =Counter(s)
    for i,c in enumerate(s):
        if count[c] == 1:
            return c
    return -1

def firstcharwithoutcounter(s):
    char_count = {}
    for ch in s:
        char_count[ch] = char_count.get(ch,0) + 1
    for k,v in char_count.items():
        if v==1:
            return k,s.index(k)
    return -1

s=input()
print(firstuniquechar(s))
print(firstcharwithoutcounter(s))