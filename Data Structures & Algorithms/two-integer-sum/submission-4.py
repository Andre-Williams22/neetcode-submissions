class Solution:

    # Example 1 
    # [3, 4, 5, 6], target = 7 
    #     ^

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numbers = {} # {3: 4, }

        for i in range(len(nums)):
            diff = target - nums[i]
            # 4 
            if diff in numbers:
                return [numbers.get(diff), i]
            numbers[nums[i]] = i 