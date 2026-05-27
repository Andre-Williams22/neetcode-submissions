class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sortedWordKey = ''.join(sorted(word))
            if sortedWordKey not in anagrams:
                anagrams[sortedWordKey] = []
            anagrams[sortedWordKey].append(word)

        return list(anagrams.values()) 