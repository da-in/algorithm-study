class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_s = list(s)
        res = []
        answer = 0

        for c in new_s:
            if c in res:
                idx = res.index(c)
                res = res[idx+1:]
                res.append(c)
            else:
                res.append(c)    
            answer = max(answer, len(res))
        return answer       
