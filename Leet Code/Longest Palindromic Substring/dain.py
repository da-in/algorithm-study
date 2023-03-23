class Solution(object):
    def longestPalindrome(self, s):
        answer = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(answer) >= j - i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    answer = s[i:j]
        return answer


# 시간초과

# class Solution(object):
#     def longestPalindrome(self, s):
#         s=list(s)
#         substr=[]
#         def isPalindrome(str):
#             for i in range(len(str)//2):
#                 if(str[i]!=str[len(str)-i-1]):
#                     return False
#             return True
#         for i in range(len(s),-1,-1):
#             for j in range(len(s)-i):
#                 if(isPalindrome(s[j:j+i+1])):
#                     return ''.join(s[j:j+i+1])
