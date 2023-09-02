import sys

N = int(sys.stdin.readline())

y = []

for i in range(N):
    y.append(int(sys.stdin.readline().split()[1]))  # y 좌표만 저장
y.append(0)

stack = [0]
result = 0

for h in y:
    height = h
    while stack[-1] > h:    # 중복되는 높이 검사
        if stack[-1] != height:
            result += 1
            height = stack[-1]  # 해당 빌딩 높이를 저장해서 다른 높이에 한해서 갯수 더하기
        stack.pop()
    stack.append(h)

print(result)
