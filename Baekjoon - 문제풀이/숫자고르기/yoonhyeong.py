import sys

N = int(input())

arr = [0]

for _ in range(N):
    arr.append(int(input()))

result = set()


def dfs(s1, s2, num):
    s1.add(num)         # 윗줄 집합에 숫자 추가
    s2.add(arr[num])    # 아랫줄 집합에 윗줄 바로 아래의 숫자 추가

    if arr[num] in s1:  # 윗줄 집합에 숫자가 있고
        if s1 == s2:    # 집합이 같다면
            result.update(s1)   # 해당 숫자 추가
            return True
        return False    # 같지 않다면 종료

    return dfs(s1, s2, arr[num])    # 현재 숫자로 윗줄 이동


for i in range(1, N + 1):
    if i not in result:
        dfs(set(), set(), i)

result = sorted(list(result))
print(len(result))
for i in result:
    print(i)



