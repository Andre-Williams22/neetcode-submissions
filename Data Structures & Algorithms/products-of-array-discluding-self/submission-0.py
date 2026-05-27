class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [None] * len(nums)
        for i in range(len(nums)):
            productSum = 1
            for j in range(len(nums)):
                if i != j:
                    productSum *= nums[j]
            
            products[i] = productSum 

        return products 
        


        