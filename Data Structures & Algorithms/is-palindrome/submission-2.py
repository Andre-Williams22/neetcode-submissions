class Solution:
    def isPalindrome(self, s: str) -> bool:
        stringList = [word.lower() for word in s if word.isalpha() or word.isnumeric()]
        s = ''.join(stringList)
        if s == s[::-1]:
            return True 
        return False 
