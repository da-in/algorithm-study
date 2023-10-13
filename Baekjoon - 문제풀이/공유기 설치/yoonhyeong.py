import sys

N, C = map(int, sys.stdin.readline().split())
X = [int(sys.stdin.readline()) for _ in range(N)]

X = sorted(X)

start = 1
end = X[-1] - X[0]

result = 0


while start <= end:
    mid = (start + end) // 2

    house = X[0]
    count = 1

    for i in range(1, N):
        if X[i] - house >= mid:
            count += 1
            house = X[i]

    if count >= C:  # 공유기 다 설치 가능할 때, 갯수 갱신 후에 거리 늘림
        start = mid + 1
        result = max(mid, result)
    else:   # 공유기 다 설치 못할 때, 거리 좁힘
        end = mid - 1

print(result)