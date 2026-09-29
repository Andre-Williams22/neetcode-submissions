class Solution:

    def encode(self, strs: List[str]) -> str:
        # for each string, 
        # store its length + a delimiter + the string itself 
        return ''.join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        while i < len(s):
            # find the position of delimitter to get length 
            j = s.find("#", i)
            length = int(s[i:j])
            # extract string using parsed length
            res.append(s[j+1:j+1+length])
            i = j + 1 + length 

        return res