class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(nlog(n))
        nums.sort()
        # O(n)
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)