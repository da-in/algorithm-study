def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []

    for i, p in enumerate(prices):
        while stack and stack[-1][0] > p:
            pop_p, pop_i = stack.pop()
            answer[pop_i] = i - pop_i
        stack.append((p, i))

    for p, i in stack:
        answer[i] = len(prices) - 1 - i

    return answer
