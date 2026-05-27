class Solution:

    def encode(self, strs: List[str]) -> str:
        combinedString = ""
        for word in strs:
            combinedString += str(len(word)) + "#" + word

        return combinedString

    def decode(self, s: str) -> List[str]:
        combinedString = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            i = j + 1 
            j = i + length
            combinedString.append(s[i:j])
            i = j
        return combinedString

