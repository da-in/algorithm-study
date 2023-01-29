def solution(numbers):
    answer = []
    stack = []
    for n in reversed(numbers):
        while stack and stack[-1] <= n:
            stack.pop()
        if stack:
            answer.append(stack[-1])
            stack.append(n)
        else:
            answer.append(-1)
            stack.append(n)

    return list(reversed(answer))


# 테스트 20 - 23 시간초과 발생한 코드

def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1, -1, -1):
        big = -1
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                big = numbers[j]
                break
        answer.append(big)

    return list(reversed(answer))
