def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    for i in range(n):
        answer.append(s // n)

    for i in range(1, (s % n) + 1):
        answer[-i] += 1

    return answer
