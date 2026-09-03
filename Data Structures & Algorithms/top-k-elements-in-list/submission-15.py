class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # get counts 
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        minHeap = []
        for freq, num in freq.items():
            heapq.heappush(minHeap, (num, freq))
            # if heap size > k, pop once to remove the smallest frequency 
            if len(minHeap) > k: 
                heapq.heappop(minHeap)
        print("heap", minHeap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res 
        
