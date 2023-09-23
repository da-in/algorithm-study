import sys
from collections import deque

R,C = map(int, sys.stdin.readline().split())
boards = [[j for j in sys.stdin.readline().rstrip('\n')] for _ in range(R)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

visited_alpha = set(boards[0][0])
# visited_alpha = [boards[0][0]]
result = 1

def dfs(x, y):
    global result
    result = max(result, len(visited_alpha))
    
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if new_x<0 or new_x>=C or new_y<0 or new_y>=R:
            continue

        if boards[new_y][new_x] in visited_alpha:
            continue

        visited_alpha.add(boards[new_y][new_x])
        dfs(new_x, new_y)
        visited_alpha.remove(boards[new_y][new_x])

dfs(0,0)
print(result)