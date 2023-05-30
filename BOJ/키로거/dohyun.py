"""

풀이시간
- 약 20분 소요

접근법
- 문자열의 길이가 생각보다 길다! 시간복잡도를 줄여야 할 듯
- 문제를 읽어보니 BOJ 에디터 문제의 접근과 거의 완전히 유사함
- 지수님의 deque 풀이에 영감을 받아 참고해서 풀이 ㅎㅎ..

회고
- 이전 문제를 잘 이해하고 넘어가면 비슷한 유형을 만났을 때 빠르게 풀이가 가능하다! 문제 대충 넘어가지말고 잘 이해하자
- 이 문제는 왜인지는 모르겠지만 sys.stdin.readline() 을 사용할 때 보다 input() 을 사용한게 더 빨랐다..?

"""

import sys
from collections import deque

n = int(sys.stdin.readline())                       # 문자열 개수 입력

for i in range(n):
    left = deque()                                  # 커서 기준 왼쪽 비밀번호
    right = deque()                                 # 커서 기준 오른쪽 비밀번호
    passwords = sys.stdin.readline().rstrip()
    
    for password in passwords:                      # 문자열을 처음부터 순서대로 검토
        if (password == '<') and left:              # 커서를 왼쪽으로 옮김 + 커서가 맨 처음에 위치하는 경우 제외
            right.appendleft(left.pop())
        elif (password == '>') and right:           # 커서를 오른쪽으로 옮김 + 커서가 맨 처음에 위치하는 경우 제외
            left.append(right.popleft())
        elif (password == '-') and left:            # 왼쪽 문자열을 제거 + 커서가 맨 처음에 위치하는 경우 제외
            left.pop()
        elif password not in (['<', '>', '-']):     # left, right 덱이 비어있을 경우 제외
            left.append(password)
    
    print(''.join(left+right))