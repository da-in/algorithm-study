N = int(input())
tower = list(map(int, input().split()))

res = [0] * N
temp = []

for i in range(N):
    while temp:
        # 안되는 경우
        if temp[-1][0] < tower[i]:
            temp.pop()
        # 되는 경우
        else:
            res[i] = temp[-1][1] + 1
            break
    temp.append([tower[i], i])

print(" ".join(map(str, res)))
