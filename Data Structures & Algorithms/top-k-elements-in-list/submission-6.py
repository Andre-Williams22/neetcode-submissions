class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 
        
        # sort numbers by frequency (highest first)
        sortedNums = sorted(freq, key=lambda x: freq[x], reverse=True)

        return sortedNums[:k]