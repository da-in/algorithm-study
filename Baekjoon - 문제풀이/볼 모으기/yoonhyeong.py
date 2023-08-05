import sys

N = int(sys.stdin.readline())

balls = [ball for ball in sys.stdin.readline().rstrip()]


result = sys.maxsize

cnt_red = 0
flag_red = False

cnt_blue = 0
flag_blue = False

for i in range(N):  # 왼쪽으로 옮길 경우
    ball = balls[i]

    if ball == 'B':
        flag_red = True

    if ball == 'R':
        flag_blue = True

    if ball == 'R' and flag_red:
        cnt_red += 1

    if ball == 'B' and flag_blue:
        cnt_blue += 1

result = min(cnt_red, cnt_blue)

cnt_red = 0
flag_red = False

cnt_blue = 0
flag_blue = False

for i in range(N-1, -1, -1): # 오른쪽으로 옮길 경우
    ball = balls[i]

    if ball == 'B':
        flag_red = True

    if ball == 'R':
        flag_blue = True

    if ball == 'R' and flag_red:
        cnt_red += 1

    if ball == 'B' and flag_blue:
        cnt_blue += 1

result = min(result, cnt_red, cnt_blue)

print(result)

