s = list(input())

cnt_a = s.count('a')
l = len(s)
s.extend(s)
res = 10000

for i in range(l):
    res = min(res, s[i:i+cnt_a].count('b'))

print(res)
