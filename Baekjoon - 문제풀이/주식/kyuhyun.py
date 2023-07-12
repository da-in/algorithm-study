N = int(input())

while N > 0:
    days = int(input())
    cost = list(map(int, input().split()))

    res = 0
    cur_max = 0
    while cost:
        val = cost.pop()
        if val > cur_max:
            cur_max = val
        elif val <= cur_max:
            res += cur_max - val
    print(res)
    N -= 1
