class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newArray = [1] * len(nums)
        # Left pass 
        left = 1 
        for i in range(len(nums)):
            newArray[i] = left
            left *= nums[i]
        # Right pass: Multiple newArray[i] by product of all elements to the right
        right = 1 
        for i in range(len(nums)-1, -1, -1):
            newArray[i] *= right 
            right *= nums[i]

        return newArray