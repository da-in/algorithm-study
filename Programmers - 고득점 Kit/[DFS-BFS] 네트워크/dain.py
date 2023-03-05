from collections import deque

def solution(n, computers):
    answer = set()
    for i in range(n):
        visit = [0 for _ in range(n)]
        q = deque([i])
        visit[i] = 1
        root = i
        while q:
            cur = q.popleft()
            root = min(cur, root)
            for j in range(n):
                if computers[cur][j] == 1 and visit[j] == 0:
                    q.append(j)
                    visit[j] = 1
        answer.add(root)

    return len(answer)
