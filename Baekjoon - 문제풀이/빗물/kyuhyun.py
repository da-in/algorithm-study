H, W = map(int, input().split(" "))
wall = list(map(int, input().split(" ")))

res = 0
for i in range(1, W-1):
    left_max = max(wall[:i])
    right_max = max(wall[i+1:])

    low = min(left_max, right_max)

    if wall[i] < low:
        res += low - wall[i]
print(res)
