# O(n) time | O(n) space where n is the size of the input array. 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # nums = [3,4,5,6], target = 7
        #           ^
        pairs = {}# { 4: 0, 

        for i in range(len(nums)): 
            diff = target - nums[i] 
            if diff in pairs: 
                return [pairs.get(diff), i]
            pairs[nums[i]] = i