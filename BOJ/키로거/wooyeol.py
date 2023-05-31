"""
    키로거
    https://www.acmicpc.net/problem/5397
    
    접근법
    무슨 알고리즘으로 풀이 할 수 있을까? -> deque을 사용해서 cursur를 기준으로 데이터 이동
    
    1. 커서 문제가 나오면 연결리스트 방식과 다음과 같이 
    cursur를 기준으로 공간을 생각하여 풀이하는 방식으로 풀이 할 수 잇을 것 같았다.

    결국 풀이는 두개의 덱을 사용한 이전 에디터 문제와 동일한 형식을 사용하여 풀이 할 수 있었다.
"""
import sys
from collections import deque

input = sys.stdin.readline

L = int(input())


answer = []
for _ in range(L):
    left,right = deque(), deque()           # 두 개의 왼쪽 오른쪽 덱을 구현
    sentence = input().strip()
    for c in sentence:
        if c == '<' and left:               # < 연산자는 왼쪽 덱의 오른쪽 요소를 오른쪽 덱의 왼쪽 삽입
            right.appendleft(left.pop())
        elif c == '>' and right:            # > 연산자는 오른쪽 덱의 왼쪽 요소를 왼쪽 덱의 오른쪽 요소에 삽입
            left.append(right.popleft())
        elif c == '-' and left:             # - 연산자는 왼쪽 덱의 오른쪽 요소 제거
            left.pop()
        elif c not in ('<','>','-'):        # 연산자가 아닌 문자는 왼쪽 덱의 오른쪽에 삽입
            left.append(c)
    answer.append(left+right)

for ans in answer:
    print("".join(ans))

