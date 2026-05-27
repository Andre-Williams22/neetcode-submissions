class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = []

        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            # skips duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1 
                    right -= 1 
                    while nums[left] == nums[left-1] and left < right:
                        left += 1 
                elif total < 0:
                    left += 1 
                else:
                    right -= 1 

        return triplets 
