class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        charSet = set()
        l = 0 
        longestSubString = 0
        for r in range(len(s)): # right pointer goes through all characters
            currCount = 0 
            while s[r] in charSet:
                # remove left from set 
                charSet.remove(s[l])
                # shrink window 
                l += 1
                currCount += 1 
            charSet.add(s[r])
            # update longestSubString
            longestSubString = max(longestSubString, r - l + 1)

        return longestSubString


