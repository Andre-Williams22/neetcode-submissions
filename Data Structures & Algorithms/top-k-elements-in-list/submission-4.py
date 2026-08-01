from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = Counter(nums)

        res = []


        # use a min-heap to get k most frequent elements
        for num, count in heapq.nlargest(k, freq.items(), key=lambda x:x[1]):
            res.append(num)
        return res
