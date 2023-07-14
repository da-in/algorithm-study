from collections import deque
x, y = map(int, input().split())

map = [0] * 200001
visit = [0] * 200001
st = deque()
st.append(x)
visit[x] = 1

while st:
    val = st.popleft()

    d = [val * 2, val - 1, val + 1]
    step = [map[val], map[val] + 1, map[val] + 1]

    for i in range(3):
        if d[i] > 200000 or d[i] < 0:
            continue
        if visit[d[i]] == 0:
            st.append(d[i])
            visit[d[i]] = 1
            map[d[i]] = step[i]

    if visit[y] == 1:
        print(map[y])
        break
