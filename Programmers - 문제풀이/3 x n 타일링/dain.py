def solution(n):
    answer = [0, 3, 11]
    if n % 2 != 0:
        return 0
    n = n // 2
    if n <= 2:
        return answer[n]
    for i in range(3, n + 1):
        answer.append(answer[-1] * 3 + sum(answer[:-1]) * 2 + 2)
    return answer[-1] % 1000000007
