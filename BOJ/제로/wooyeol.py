"""
    제로
    https://www.acmicpc.net/problem/10773
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> 단순구현
"""

import sys
input = sys.stdin.readline

K = int(input().strip())

# Targets 리스트를 스택으로 사용한다.
targets = []
for _ in range(K):
    target = int(input().strip())

    # target == 0 이라면 target append 아니라면 pop
    if target:
        targets.append(target)
    else:
        targets.pop()

# 전체 원소 덧셈 값 반환
print(sum(targets))