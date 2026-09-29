class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        counts = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in counts:
                return [counts.get(diff), i]
            # add to dictionary 
            counts[nums[i]] = i
        return []
