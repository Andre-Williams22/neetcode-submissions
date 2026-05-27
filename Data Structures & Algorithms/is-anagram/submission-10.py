class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        p1 = 0 
        p2 = 0 
        while p1 < len(sorted_s) and p2 < len(sorted_t):
            if sorted_s[p1] == sorted_t[p2]:
                p1 += 1 
                p2 += 1 
            else:
                p1 += 1 

        return p1 == p2 
        


# aaccerr
# ^  
# aaccerr
# ^