class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for l in s:
            if l.isalnum():
                newString += l.lower()
        return newString == newString[::-1]


