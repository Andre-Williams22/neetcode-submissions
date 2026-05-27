class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s = list(sorted(s))
        t = list(sorted(t))

        p1 = 0 
        p2 = 0 
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1 
                p2 += 1 
            else:
                return False 
        
        return p1 == len(s) and p2 == len(t)

        

        