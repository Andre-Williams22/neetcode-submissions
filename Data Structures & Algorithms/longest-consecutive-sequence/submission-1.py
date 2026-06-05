class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # instantiate set 
        numSet = set(nums)
        longest = 0

        for i in range(len(nums)):
            # check if it's a start of a sequence
            if (nums[i] - 1) not in numSet:
                # no left neighbor exist
                length = 0 # start counter
                while (nums[i] + length) in numSet:
                    length += 1 

                longest = max(length, longest)
        return longest
