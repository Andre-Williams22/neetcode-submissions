class Solution:
    # O(n log n) solution | O(n) space
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = {}

        # traverse input list
        for word in strs:
            # sort string 
            sortedWord = "".join(sorted(word))
            # check if string exist in dict
            if sortedWord in anagrams: 
                anagrams[sortedWord].append(word) 
                # anagrams[sortedKey].append([unsorted original string])
            else:
                anagrams[sortedWord] = [word]

        for key, value in anagrams.items():
            result.append(value)

        return result