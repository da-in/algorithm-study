import sys

N = int(input())

RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N):
    RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]  # 빨간색 고를 경우
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]  # 초록색 고를 경우
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]  # 파란색 고를 경우

print(min(RGB[N-1][0], RGB[N-1][1], RGB[N-1][2]))
