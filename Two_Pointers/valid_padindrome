'''
A phrase is a palindrome if, 
after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    ====
    Thought Process
    1. Convert chars in string to lower case.
    2. Remove all spaces, and comma.
    3. Using two pointers, start and end to check whether they are equal
    4. Return True after the while loop
'''
import re

def valid_padindrome(s: str):
    new_str = s.replace(" ", "") #Prevent the case when there is all space chars
    if len(new_str) == 0:
        return True
    pattern = '[{}|~!-/:-@[\]^-`]' #Using pattern matching based on ASCII Table
    s = re.sub(pattern, '', new_str) #replace the pattern with empty string
    s = s.lower() #convert to lower cases
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


print(valid_padindrome("race a car"))
