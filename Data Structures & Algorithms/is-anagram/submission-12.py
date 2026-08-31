class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Two Pointers
        # Hashtable 

        s1 = {}
        s2 = {}

        for string in s:
            s1[string] = s1.get(string, 0) + 1 

        for string in t:
            s2[string] = s2.get(string, 0) + 1 
        
        return s1 == s2
        
