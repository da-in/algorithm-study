from collections import deque

N, K = map(int, input().split())
l = list(map(int, input().split()))
ans = 0
visit = [0] * (max(l) + 1)
d = deque()

for val in l:
    if visit[val] == K:
        ans = max(ans, len(d))
        while d[0] != val:
            visit[d.popleft()] -= 1
        visit[d.popleft()] -= 1
    d.append(val)
    visit[val] += 1

ans = max(ans, len(d))
print(ans)
