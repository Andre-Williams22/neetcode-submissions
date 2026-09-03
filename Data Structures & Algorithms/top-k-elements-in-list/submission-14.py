class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # get counts 
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 
        
        arr = []
        for key, val in freq.items():
            arr.append([val, key]) 
        # sort keys and values
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        
