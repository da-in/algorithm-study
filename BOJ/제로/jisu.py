"""
21:36 -> 21:40

Key Idea : 리스트를 스택으로 사용
K번 수를 입력받아 0인 경우 스택에서 마지막 원소 pop, 이외에는 스택에 해당 수를 추가

이는 입력 받은 수가 0인 경우 스택이 비어있지 않음이 보장되어 있기 때문에 가능하다
이게 보장되어있지 않다면, pop을 할 때마다 스택이 비어있는지를 검사해야 한다.
"""

import sys

input = sys.stdin.readline

def main():

    K = int(input().rstrip())                           # K번 입력받을 것입니다
    stack = []

    for _ in range(K):                                  # K번 입력 받기
        num = int(input().rstrip())
        stack.pop() if num == 0 else stack.append(num)  # 입력 받은 수가 0이면 스택의 마지막 원소 pop, 이외에는 추가
                                                        # 0일 때는 스택이 비어있지 않음이 보장되어있으니 가능한 코드

    print(sum(stack))   # 최종 스택 내 수들의 합 출력

main()
    