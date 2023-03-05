from collections import deque

def solution(number, k):
    stack = []
    number = deque(list(number))
    while k and number:
        n = number.popleft()
        while k and stack and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)

    answer = stack + list(number)
    for _ in range(k):
        answer.pop()

    return "".join(answer)


# 시간초과 코드
# from collections import deque

# def solution(number, k):
#     answer = []
#     number = deque(list(number))
#     while k and number:
#         max_num = max(list(number)[: k + 1])
#         for _ in range(k):
#             if number[0] < max_num:
#                 number.popleft()
#                 k -= 1
#             else:
#                 answer.append(number.popleft())
#                 break
#     answer = answer + list(number)
#     for _ in range(k):
#         answer.pop()
#     return "".join(answer)
