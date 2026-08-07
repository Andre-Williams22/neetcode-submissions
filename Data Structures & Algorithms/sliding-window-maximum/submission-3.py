class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] # 3
        queue = deque() # [1, 2]
        l = 0  

        # nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3 

        for i, num in enumerate(nums):
            # remove indices out of the curr window
            while queue and queue[0] <= i - k:
                queue.popleft()

            # remove vals that are less that the curr value 
            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(i) # adds new idx to window
            # append the max for window 
            if i >= k - 1: 
                res.append(nums[queue[0]])


        return res 

            
            
