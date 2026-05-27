class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        anagram_dict = {}

        if len(s) != len(t):
            return False

        for letter in s:
            if letter not in anagram_dict:
                anagram_dict[letter] = 0
            anagram_dict[letter] += 1 

        for letter in t:
            if letter in anagram_dict:
                anagram_dict[letter] -= 1 
        
        return max(anagram_dict.values())==0
        

    
