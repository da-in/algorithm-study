class Solution:
    def longestPalindrome(self, s: str) -> str:
        def calc(i,j):
            while i-1>=0 and j+1<len(s) and s[i-1]==s[j+1]:
                i-=1
                j+=1
            return s[i:j+1]
        answer=""
        for i in range(len(s)):
            temp=calc(i,i)
            if i+1<len(s) and s[i]==s[i+1]:
                temp2=calc(i,i+1)
                if len(temp2)>len(temp):
                    temp=temp2
            if len(temp)>len(answer):
                answer=temp
        return answer
    