import sys 
from collections import deque


input = sys.stdin.readline

def solution():
    """key idea
    자료구조 하나만을 활용한다면, 문자 사이에 삽입, 제거하는 연산의 복잡도가 각 O(N)이기 때문에 시간 초과가 발생할 것이다.
    또, 경험상 굉장히 헷갈려서 머리아팠던 기억이 있다.. 

    두 개의 deque을 활용해서 커서 기준 왼쪽, 오른쪽 문자열로 활용하자!
    deque은 double linked list기반 자료구조이기 때문에 오른쪽 왼쪽 어느 곳에서 삽입, 삭제 연산을 진행하더라도 O(1)이다.
    이를 통해 효율적이면서 직관적으로 문제를 해결할 수 있다.
    """
    left = deque(input().rstrip())   # 커서 기준 왼쪽 문자열
    right = deque()   # 커서 기준 오른쪽 문자열
    N = int(input())
    for _ in range(N):
        ops = input().rstrip().split()
        if ops[0] == 'L' and left:     # 커서를 왼쪽으로 옮긴다 : 왼쪽 맨 뒤 원소를 오른쪽 첫 번째 원소로 삽입한다.
            right.appendleft(left.pop())
        if ops[0] == 'D' and right:    # 커서를 오른쪽으로 옮긴다 : 오른쪽 맨 앞 원소를 왼쪽 맨 뒤 원소로 삽입한다.
            left.append(right.popleft())
        if ops[0] == 'B' and left:
            left.pop()
        if ops[0] == 'P':
            left.append(ops[1])

    print(''.join(left+right))

if __name__ == "__main__":
    solution()

