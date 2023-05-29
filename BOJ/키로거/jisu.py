import sys
from collections import deque

input = sys.stdin.readline

T = int(input())    # 테스트 케이스 수

for _ in range(T):
    left, right = deque(), deque()      # 각각 커서 왼쪽, 오른쪽 문자열을 담을 리스트(덱)

    ops = list(input().rstrip())
    for op in ops:
        if op == '<':                   # (주의) if op=='<' and left 와 같이 쓰면 left가 비어있을 때 else 분기로 가게 됨
            if left:
                right.appendleft(left.pop())
        elif op == '>':
            if right:
                left.append(right.popleft())
        elif op == '-':
            if left:
                left.pop()
        else:
            left.append(op)

    print(''.join(left+right))  # 커서 기준 왼쪽, 오른쪽 문자열을 합쳐서 join
