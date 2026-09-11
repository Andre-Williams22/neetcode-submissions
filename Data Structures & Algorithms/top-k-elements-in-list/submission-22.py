class Solution:
    # Total: O(n log k) time | O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        # O(n) time
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 

        heap = []
        # Log (N) time operation
        for num in freq:
            heapq.heappush(heap, (freq.get(num), num)) # count is first in heap, then key 2nd.
            if len(heap) > k:
                heapq.heappop(heap)
    
        res = []
        # O(k) time 
        for i in range(k):
            print("heap:", heap, "res:", res)
            element = heapq.heappop(heap)[1] # grab key not count 
            res.append(element)
        return res