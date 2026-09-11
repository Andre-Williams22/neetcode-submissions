class Solution:
    # O(n) time | O(n) space 
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # [2,20,4,10,3,4,5]
                            #             ^
        longestSeq = 0 # 2
        # check to see if num -1 exists to find beginning of sequence
        for num in nums:
            # look back to see start of sequence
            if (num-1) not in numSet:
                length = 0
                # continue moving forward up 1 consecutively 
                while (num + length) in numSet:
                    length += 1 
                longestSeq = max(longestSeq, length)

        return longestSeq
