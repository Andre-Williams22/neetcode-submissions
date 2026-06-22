class Solution:
    def isValid(self, s: str) -> bool:
        
        chars = {"]":"[", "}":"{", ")":"("}
        stack = [] #'['

        for char in s:
            if char in chars:
                if stack and stack[-1] == chars[char]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(char)
        if len(stack) == 0:
            return True 
        return False 
           

            