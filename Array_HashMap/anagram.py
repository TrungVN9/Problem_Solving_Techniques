'''
Given two strings s and t, 
return  true if t is an anagram of s,
        false otherwise.
        
    Input: s = "anagram", t = "nagaram"
    Output: true
    
    Input: s = "rat", t = "car"
    Output: false

    Thought Process:
    // Use hash map
    // count the number of chars that appears in the hash map
    // then check the number of chars in both s and t
    // if they all equal --> True, Otherwise False
'''
def check_anagram(s: str, t: str) -> bool:
# def check_anagram(s: str, t: str):
    #Check if the length of string s and t
    if len(s) != len(t):
        return False
    
    hash_map_t = {}
    hash_map_s = {}

    for index in range(len(s)):
        hash_map_s[s[index]] = 1 + hash_map_s.get(s[index], 0) #if s[index] in hash_map_s
        hash_map_t[t[index]] = 1 + hash_map_t.get(t[index], 0)
   
    if (hash_map_t == hash_map_s):
        return True
    return False
# check_anagram("anagram", "nagaram")
print(check_anagram("anagram", "nagaram"))