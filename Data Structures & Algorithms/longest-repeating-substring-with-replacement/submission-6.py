class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {} # tracks count of each char in window 
        maxf = 0 # max freq of each char in window 
        res = 0 
        l = 0 # left pointer 

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1 # gets frequencies
            maxf = max(maxf, count[s[r]])

            # swap out with k and shrink the window 
            while (r - l + 1) - maxf > k: # if more than k replacements needed, shrink window 
                count[s[l]] -= 1 
                l += 1 # moves left pointer up 
            
            res = max(res, r - l + 1) # update result as move window 
        
        return res 
