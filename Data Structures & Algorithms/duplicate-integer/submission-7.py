class Solution:
    # O(n) time | O(n) space
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seenNums = set()

        for num in nums:
            if num in seenNums:
                return True 
            seenNums.add(num)
        return False 