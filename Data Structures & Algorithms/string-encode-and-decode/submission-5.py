class Solution:

    # O(n)
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # adds lenth and # as delimitter before each word
            res += str(len(s)) + "#" + s
        return res 


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            # find delimitter 
            j = i 
            while s[j] != "#":
                j += 1 
            # how many following chars we have to read after j
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res



