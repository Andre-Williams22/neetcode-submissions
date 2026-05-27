class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triplets = list()

        for i in range(len(nums)):
            # remove duplicates & stay in-bounds
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1 
                elif total > 0:
                    right -= 1 
                else:
                    # equal 
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                
                    while nums[left] == nums[left-1] and left < right:
                            left += 1

        return triplets 
