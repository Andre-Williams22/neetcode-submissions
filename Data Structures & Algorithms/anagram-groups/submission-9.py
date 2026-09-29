class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {} # O(n) space 

        for word in strs:
            sortedWord = "".join(sorted(word)) # O(n log n)
            if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
            else:
                anagrams[sortedWord] = [word]

        return list(anagrams.values()) 