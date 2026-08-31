class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1 

        while l < r:
            currTotal = numbers[l] + numbers[r]

            if currTotal == target:
                return [l+1, r+1]
            elif currTotal < target: 
                l += 1 
            else:
                r -= 1  


