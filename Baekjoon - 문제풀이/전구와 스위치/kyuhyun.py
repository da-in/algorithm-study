N = int(input())
start = input()
end = input()


def change(val):
    if val == 0:
        return 1
    return 0


def switch(val):
    cnt = 0
    for i in range(N-1):
        if i != N - 2:
            if val[i] != int(end[i]):
                val[i] = change(val[i])
                val[i+1] = change(val[i+1])
                val[i+2] = change(val[i+2])
                cnt += 1
        else:
            if val[i] != int(end[i]):
                val[i] = change(val[i])
                val[i+1] = change(val[i+1])
                cnt += 1
    return cnt, val


# 0번 스위치를 누른 경우
val = list(map(int, start))
val[0] = change(val[0])
val[1] = change(val[1])
res_0, new_val = switch(val)
if "".join(map(str, new_val)) == end:
    res_0 += 1
else:
    res_0 = -1

# 0번 스위치를 누르지 않은 경우
val = list(map(int, start))
res_1, new_val = switch(val)
if "".join(map(str, new_val)) != end:
    res_1 = -1

if res_0 * res_1 < 0:
    print(max(res_0, res_1))
else:
    print(min(res_0, res_1))
