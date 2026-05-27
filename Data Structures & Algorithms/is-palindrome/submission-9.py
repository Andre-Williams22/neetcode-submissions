class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(string.lower() for string in s if string.isalpha() or string.isnumeric())

        if cleaned_s == cleaned_s[::-1]:
            return True
        return False