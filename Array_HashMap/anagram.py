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

    return hash_map_t == hash_map_s
# check_anagram("anagram", "nagaram")
# print(check_anagram("anagram", "nagaram"))

'''
    Group Anagram
    Given an array of strings strs, group the anagrams together. 
    You can return the answer in any order.

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    Input: strs = [""]
    Output: [[""]]
    
    Input: strs = ["a"]
    Output: [["a"]]

    Thought Process:
    1. Implement exactly check anagram -> to count the number of chars appear in the str
    2. 
'''
# def group_anagram(strs: list[str]) -> list[list[str]]:
def group_anagram(strs: list[str]):
    hash_map_strs = {}
    for word in strs:
        for index in range(len(word)):
            hash_map_strs[word[index]] = 1 + hash_map_strs.get(word[index], 0)
    print(hash_map_strs)
group_anagram(["eat","tea","tan","ate","nat","bat"])