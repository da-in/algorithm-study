N, d, k, c = map(int, input().split(" "))

sushi = []
s = set()
res = 0
second = 0


for i in range(N):
    sushi.append(int(input()))

sushi.extend(sushi)


for i in range(N):
    s = set(sushi[i: (i+k)])
    if c not in s:
        res = max(res, len(s))
    else:
        second = max(second, len(s))
    s.clear()

if res >= second and d >= c:
    print(res + 1)
else:
    print(second)
