import sys
input = sys.stdin.readline

left = list(input().strip())
right = []
n = int(input())

for i in range(n):
    line = input().strip().split()
    command = line[0]

    if command == 'P': # 문자를 커서 왼쪽에 추가함
        left.append(line[1])
    elif command == 'L': # 커서를 왼쪽으로 한 칸 옮김
        if left:
            right.append(left.pop())
    elif command == 'D': # 커서를 오른쪽으로 한 칸 옮김
        if right:
            left.append(right.pop())
    else: # 커서 왼쪽에 문자를 삭제함
        if left:
            left.pop()

left += right[::-1]
print(''.join(left))