class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = s[0]
        def palindrome(left, right):
            while left > -1 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]

        for i in range(len(s)-1):
            answer = max(answer, palindrome(i, i+1), palindrome(i, i+2), key=len)

        return answer 
