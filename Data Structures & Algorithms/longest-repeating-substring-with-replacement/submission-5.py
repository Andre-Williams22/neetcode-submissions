class Solution:
        # O(n) Time where n is input of string | O(m) Space where m is number of unique characters
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {} # {A:4, B:3}
        maxf = 0 # track max freq
        res = 0 # final result
        l = 0 # left pointer of window
        
        # count frequency
        for r in range(len(s)):
            charFreq[s[r]] = 1 + charFreq.get(s[r], 0)
            # update max tracker
            maxf = max(maxf, charFreq[s[r]])
            # sliding window
            while (r - l + 1) - maxf > k:
                charFreq[s[l]] -= 1 
                l += 1 
            res = max(res, r-l+1)
        return res
    
                
                
        

        