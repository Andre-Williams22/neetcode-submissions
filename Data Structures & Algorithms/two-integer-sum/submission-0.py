class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numbers:
                return [numbers.get(diff), i]
            numbers[nums[i]] = i  
        return numbers 
        