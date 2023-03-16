def solution(s):
    answer = []
    
    for i in range(len(s)):
        if i == 0:
            answer.append(s[i])
        elif s[i] != s[i-1]:
            answer.append(s[i])
    return answer