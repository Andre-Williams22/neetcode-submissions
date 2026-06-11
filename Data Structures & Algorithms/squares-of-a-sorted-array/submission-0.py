class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squaresNum = [1] * len(nums)
        l = 0 
        r = len(nums)-1
        pos = len(nums)-1

        while l <= r: 
            # check abs value of larger vs smaller nums
            if abs(nums[l]) > abs(nums[r]):
                # fill nums backwards
                squaresNum[pos] = nums[l] * nums[l]
                l += 1 
            else:
                squaresNum[pos] = nums[r] * nums[r]
                r -= 1 
            pos -= 1 
        return squaresNum


            

