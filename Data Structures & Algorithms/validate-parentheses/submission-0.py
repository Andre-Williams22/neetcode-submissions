class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] #'['
        hashtable = {'(': ')', '{': '}', '[':']'}

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                topItem = stack.pop()
                if hashtable.get(topItem) != char:
                    return False 
        return len(stack) == 0
