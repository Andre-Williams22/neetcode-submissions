class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Two Pointers Solution 
        p1 = 0 
        p2 = len(numbers)-1 

        while p1 < p2: 
            currSum = numbers[p1] + numbers[p2]
            if currSum == target: 
                return [p1+1, p2+1]
            elif currSum < target: 
                p1 += 1 
            else: # current sum is too big
                p2 -= 1
        return []