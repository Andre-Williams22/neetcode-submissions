import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elementCounts = {}
        for num in nums: 
            elementCounts[num] = elementCounts.get(num, 0) + 1 
        print("dict: ", elementCounts)

        heap = []
        for num in elementCounts:
            heapq.heappush(heap, (elementCounts[num], num))
            if len(heap) > k: # keep adding to heap until k is reached
                heapq.heappop(heap)

        print("heap elements: ", heap)

        res = []
        for _ in range(k): 
            res.append(heapq.heappop(heap)[1]) # pop and take the number, not the count
        print("res", res)
        return res
