class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqElements = {}

        for num in nums:
            if num not in freqElements:
                freqElements[num] = 0
            freqElements[num] += 1 
        
        sortedDict = sorted(freqElements, key=freqElements.get, reverse=True)
        topK = [num for num in sortedDict[:k]]

        return topK

