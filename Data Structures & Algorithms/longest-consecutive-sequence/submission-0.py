class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longestSequence = 0 

        for num in nums:
            streak, curr = 0, num 
            while curr in elements:
                streak += 1 
                curr += 1
            longestSequence = max(longestSequence, streak)

        return longestSequence