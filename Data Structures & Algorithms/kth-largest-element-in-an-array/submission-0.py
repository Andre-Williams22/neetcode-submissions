class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse=True)
        
        index = k - 1
        kLargest = nums[index]

        return kLargest