import sys

# M: 가로, N: 세로
# 1:익, 0:노익, -1:없음
M,N = map(int, sys.stdin.readline().split())
tomatos = []
all_1, cant_1 = True, True

for _ in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    tomatos.append(t)

    if all_1 and 0 in t:
        all_1 = False
    if cant_1 and 1 in t:
        cant_1 = False

if all_1:
    print(0)
    exit(1)
if cant_1:
    print(-1)
    exit(1)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if new_x<0 or new_x>=M or new_y<0 or new_y>=N:
            continue

        if tomatos[new_y][new_x] == -1:
            continue

        tomatos[new_y][new_x] = 1
    print(tomatos)

day = 0

while(True):
    day+=1
    do = False
    for i in range(N):
        for j in range(M):
            if tomatos[i][j]==1:
                bfs(j,i)

    for tomato in tomatos:
        if 0 in tomato:
            do = True

    if not do:
        break

print(day)