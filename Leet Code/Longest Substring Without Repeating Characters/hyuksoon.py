from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data=dict()
        idx=0
        answer=0
        for i,sub in enumerate(s):
            if sub in data:
                answer=max(answer,i-idx)
                while sub in data:
                    del(data[s[idx]])
                    idx+=1
                
            data[sub]=True
        answer=max(answer,len(s)-idx)
        return answer
