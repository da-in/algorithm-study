import sys

N = int(sys.stdin.readline().rstrip())
before = list(map(int, sys.stdin.readline().rstrip()))
after = list(map(int, sys.stdin.readline().rstrip()))


def switch(arg_before, arg_after):
    temp_before = arg_before[:]
    answer = 0

    for i in range(1, N):
        if temp_before[i - 1] == arg_after[i - 1]:  # 이전 전구가 같다면 다음 단계 진행
            continue

        for j in range(i - 1, i + 2):
            if j < N:
                temp_before[j] = int(not temp_before[j])

        answer += 1

    if temp_before == arg_after:
        return answer
    else:
        return sys.maxsize


result = switch(before, after)  # 첫번째 스위치 안누른 경우

before[0] = int(not before[0])  # 첫번째 스위치 누른 경우
before[1] = int(not before[1])

result = min(result, switch(before, after) + 1)

if result == sys.maxsize:
    print(-1)
else:
    print(result)
