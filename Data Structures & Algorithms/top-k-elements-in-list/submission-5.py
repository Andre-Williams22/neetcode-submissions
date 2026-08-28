from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)
        res = []

        for num, count in freq.most_common(k):
            res.append(num)

        return res
