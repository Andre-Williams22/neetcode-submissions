from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = {}
        # count of chars in t 
        t_count = Counter(t) 
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        l = 0

        # exand our window with r
        for r, c in enumerate(s):
            # get frequencies
            window[c] = window.get(c, 0) + 1 
            # check if current char meets t's requirement
            if c in t_count and window[c] == t_count[c]:
                have += 1 
            # kinda shrink the winodow from left
            while have == need: 
                # update result if smaller window is found 
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                # remove leftmost char from window
                window[s[l]] -= 1 
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1 
                l += 1 
        l, r = res 
        if res_len != float("inf"):
            return s[l:r+1]
        else:
            return ""