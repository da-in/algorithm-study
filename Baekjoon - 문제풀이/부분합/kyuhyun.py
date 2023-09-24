n, s = map(int, input().split(" "))
num = list(map(int, input().split(" ")))

left = 0
right = 0
res_len = 100001
total = num[0]

while True:
    if total < s:
        right += 1
        if right == n:
            break
        total += num[right]
    else:
        total -= num[left]
        res_len = min(res_len, right - left + 1)
        left += 1

if res_len == 100001:
    print(0)
else:
    print(res_len)
