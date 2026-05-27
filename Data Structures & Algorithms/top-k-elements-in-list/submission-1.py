class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elements = {} # {1:1, 2:2, 3:3}
 
        for num in nums: 
            elements[num] = elements.get(num, 0) + 1 
            if num not in elements:
                elements[num] = 0
            elements[num] += 1 

        sortedElements = sorted(elements.keys(), key=lambda x: elements[x], reverse=True)
        return sortedElements[:k]