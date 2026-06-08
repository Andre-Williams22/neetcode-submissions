class Solution:
    # O(n) time | O(m) space
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        longestSubstring = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            charSet.add(s[r])
            longestSubstring = max(longestSubstring, r - l + 1)

        return longestSubstring  
            