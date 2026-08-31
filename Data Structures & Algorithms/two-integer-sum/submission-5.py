class Solution:

    # Example 1 
    # [3, 4, 5, 6], target = 7 
    #     ^
    # O(n) time | O(n) space
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = {} 

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numbers:
                return [numbers.get(diff), i]
            numbers[nums[i]] = i 