import sys
from collections import deque

N = int(input())
tower_list = list(map(int, sys.stdin.readline().split()))

tower_q = deque([(N-1, tower_list[-1])])
answer_list = [0 for _ in range(N)]

for idx, new_tower in enumerate(tower_list[::-1][1:]):
    while tower_q:
        old_idx, old_tower = tower_q.pop()
        if old_tower<=new_tower:
            answer_list[old_idx] = N-idx-1
        else:
            tower_q.append([old_idx, old_tower])
            break
    tower_q.append([N-idx-2, new_tower])

for i in answer_list:
    print(i, end=' ')