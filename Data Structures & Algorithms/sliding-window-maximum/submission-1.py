from collections import deque

# O(n) time | O(k) Space

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # stores indices
        res = []
        for i, num in enumerate(nums):
            # remove indices out of a window 
            if dq and dq[0] == i - k:
                dq.popleft()
            # remove smaller numbers from back 
            while dq and nums[dq[-1]] < num:
                # pop from right side 
                dq.pop()
            dq.append(i) # add to right
            # add max num for current window 
            if i >= k - 1: 
                res.append(nums[dq[0]])
        return res
        