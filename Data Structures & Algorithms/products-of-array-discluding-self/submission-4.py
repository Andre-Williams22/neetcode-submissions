class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums) # initialize result array with 1s 

        # left-to-rgiht store prefix products 
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix # set curr res[i] to product of all left elements 
            prefix *= nums[i] # update prefix product

        suffix = 1 
        for i in range(len(nums)-1, -1, -1): #traverse backwards right-to-left
            res[i] *= suffix # multiply by product of all right nums 
            suffix *= nums[i]
        
        return res 