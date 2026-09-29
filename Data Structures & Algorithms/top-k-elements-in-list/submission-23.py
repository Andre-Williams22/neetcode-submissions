class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1 

        minHeap = []
        # push values into heap O(log n) time 
        for key, value in frequency.items():
            heapq.heappush(minHeap, (value, key))

            while len(minHeap) > k:
                heapq.heappop(minHeap)

        print("heap", minHeap)
        res = []
        while len(res) < k:
            res.append(minHeap.pop()[1])
        return res 