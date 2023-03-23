class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_s = list(s)
        res = []
        max = 0

        for c in new_s:
            if c in res:
                idx = res.index(c)
                res = res[idx+1:]
                res.append(c)
            else:
                res.append(c)    
            if max < len(res):
                max = len(res)
        return max        
