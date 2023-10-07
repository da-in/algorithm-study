from itertools import combinations

n, m = map(int, input().split(" "))

city = []

for _ in range(n) :
    tmp = list(map(int, input().split(" ")))
    city.append(tmp)

res = 99999
home = []
chick = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
            continue
        if city[i][j] == 2:
            chick.append([i, j])

for c in combinations(chick, m):
    total_chick = 0
    for h in home:
        len_chick = 999
        for i in range(m):
            len_chick = min(len_chick, abs(c[i][0]-h[0]) + abs(c[i][1]-h[1]))
        total_chick += len_chick
    res = min(total_chick, res)
print(res)

