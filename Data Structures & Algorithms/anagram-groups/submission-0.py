class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}

        for word in strs: 
            sortedWord = "".join(sorted(word))
            if sortedWord in hashtable:
                hashtable[sortedWord].append(word)
            else:
                hashtable[sortedWord] = [word]

        return list(hashtable.values())
            