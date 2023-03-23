class Solution(object):
    def lengthOfLongestSubstring(self, s):
        answer = 0
        window = []
        s = list(s)
        for cur in s:
            if cur not in window:
                window.append(cur)
            else:
                window = window[window.index(cur) + 1 :]
                window.append(cur)
            print(window)
            answer = max(answer, len(window))
        return answer
