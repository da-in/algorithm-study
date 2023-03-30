class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        start  = answer = 0
        n = len(s)
        for i in range(n):
            if s[i] in dict:
                start = max(start,dict[s[i]]+1)
            answer = max(answer, i-start+1)
            dict[s[i]] = i
        return answer    