class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        numHash = set(nums)
        for i in range(len(nums)):
            if i not in numHash:
                return i 
        return len(nums)