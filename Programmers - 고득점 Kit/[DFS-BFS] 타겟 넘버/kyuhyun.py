from collections import deque

def BFS(numbers, target):

    answer = 0
    queue = deque()
    queue.append([0, 0])

    while queue:
        idx, v = queue.popleft()

        if idx < len(numbers):
            queue.append([idx + 1,  v + numbers[idx]])
            queue.append([idx + 1,  v - numbers[idx]])

        if idx == len(numbers) and v == target:
            answer += 1
    return answer


def DFS(numbers, target):

    answer = 0
    stack = []
    stack.append([0, 0])

    while stack:
        idx, v = stack.pop()

        if idx < len(numbers):
            stack.append([idx + 1, v + numbers[idx]])
            stack.append([idx + 1, v - numbers[idx]])

        if idx == len(numbers) and v == target:
            answer += 1
    return answer


return BFS(numbers, target)
return DFS(numbers, target)
