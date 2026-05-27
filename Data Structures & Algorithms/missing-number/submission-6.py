class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(nlog(n))
        nums.sort()
        # O(n)
        for i in range(len(nums)+1):
            try: 
                if nums[i] != i:
                    return i
            
            except Exception as e:
                return i 