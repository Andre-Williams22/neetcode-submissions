class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n # Intializing our arrays of 0s 
        stack = [] # stack to store indices 

        for i, temp in enumerate(temperatures):
            # while stack is not empty and current > temp at stack's top idx
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop() # get index from stack 
                result[idx] = i - idx # calculate days waited
            stack.append(i) # push current idx to stack 

        return result
