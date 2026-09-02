class Solution:
    # O(n log n) solution | O(nk) space (n=num words, k=max word length)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

        return list(anagrams.values())